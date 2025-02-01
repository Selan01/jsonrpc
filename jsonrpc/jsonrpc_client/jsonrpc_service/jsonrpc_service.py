import os
import http.client
import ssl
import json
import tempfile
from django.conf import settings


class JsonRpcClient:
    def __init__(self, host):
        self.host = host
        self.cert_content = settings.CERTIFICATE_CONTENT
        self.key_content = settings.PRIVATE_KEY_CONTENT

    def _create_connection(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        cert_file = self._temp_cert_file(self.cert_content)
        key_file = self._temp_key_file(self.key_content)

        context.load_cert_chain(certfile=cert_file, keyfile=key_file)
        self._remove_temp_files(cert_file, key_file)

        return http.client.HTTPSConnection(self.host, context=context)

    def _temp_cert_file(self, cert_content):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".crt") as temp_cert_file:
            temp_cert_file.write(cert_content.encode())
            temp_cert_file.close()
            return temp_cert_file.name

    def _temp_key_file(self, key_content):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".key") as temp_key_file:
            temp_key_file.write(key_content.encode())
            temp_key_file.close()
            return temp_key_file.name

    def _remove_temp_files(self, cert_file, key_file):
        try:
            os.remove(cert_file)
            os.remove(key_file)
        except OSError as e:
            print(f"Ошибка при удалении временных файлов: {e}")

    def call_method(self, method, params=None, endpoint="/api/v2/"):
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params if params else {},
            "id": 1
        }

        json_payload = json.dumps(payload)
        conn = self._create_connection()

        headers = {
            'Content-Type': 'application/json',
            'Content-Length': str(len(json_payload)),
        }

        try:
            conn.request("POST", endpoint, body=json_payload, headers=headers)
            response = conn.getresponse()
            response_data = response.read().decode()

            result = json.loads(response_data)

            if "error" in result:
                raise ValueError(f"Ошибка API: {result['error']}")

            return result['result']

        except ValueError as ve:
            print(f"Ошибка json: {ve}")
            return {"error": str(ve)}
        except http.client.HTTPException as he:
            print(f"Ошибка HTTP: {he}")
            return {"error": str(he)}
        except Exception as e:
            print(f"Ошибка запроса: {e}")
            return {"error": str(e)}
        finally:
            conn.close()
