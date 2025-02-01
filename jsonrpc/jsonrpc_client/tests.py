from django.test import TestCase
from unittest.mock import patch
from .jsonrpc_service.jsonrpc_service import JsonRpcClient
from .forms import JsonRpcForm
from django.urls import reverse

class JsonRpcClientTest(TestCase):
    @patch.object(JsonRpcClient, 'call_method')
    def test_successful_api_call(self, mock_call_method):
        mock_call_method.return_value = {'result': 'успех'}
        client = JsonRpcClient(host='slb.medv.ru')
        response_data = client.call_method(method='auth.check', params={'username': 'test', 'password': 'test'})
        self.assertEqual(response_data, {'result': 'успех'})
        mock_call_method.assert_called_once_with(method='auth.check', params={'username': 'test', 'password': 'test'})

    @patch.object(JsonRpcClient, 'call_method')
    def test_api_call_with_error(self, mock_call_method):
        mock_call_method.return_value = {'error': 'Неверные данные'}
        client = JsonRpcClient(host='slb.medv.ru')
        response_data = client.call_method(method='auth.check', params={'username': 'test', 'password': 'wrongpassword'})
        self.assertEqual(response_data, {'error': 'Неверные данные'})
        mock_call_method.assert_called_once_with(method='auth.check', params={'username': 'test', 'password': 'wrongpassword'})


class JsonRpcFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'method': 'auth.check',
            'params': '{"username": "test", "password": "test"}'
        }
        form = JsonRpcForm(data=form_data)
        self.assertTrue(form.is_valid())


class JsonRpcFormViewTest(TestCase):
    def test_jsonrpc_form_view_invalid(self):
        with patch('jsonrpc_client.views.JsonRpcClient.call_method') as mock_call_method:
            mock_call_method.return_value = {'error': 'Неверные данные'}

            response = self.client.post(reverse('index'), {
                'method': 'auth.check',
                'params': '{"username": "test", "password": "wrongpassword"}'
            })

            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Попытка авторизации не удалась')
