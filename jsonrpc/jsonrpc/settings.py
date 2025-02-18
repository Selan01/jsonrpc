"""
Django settings for jsonrpc project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$0!+%u+&+1a3_1ily!(l_no-pah0uu4eo1^95ug372rrrl+z*r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'jsonrpc_client',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jsonrpc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jsonrpc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CERTIFICATE_CONTENT = """
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number: 390579 (0x5f5b3)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=RU, ST=Ufa, L=Ufa, O=slb, CN=slb/emailAddress=support@slb.medv.ru
        Validity
            Not Before: Jun 24 12:00:19 2024 GMT
            Not After : Jun 24 12:00:19 2025 GMT
        Subject: C=RU, ST=Moscow, L=Moscow, O=Test, CN=test@test.test
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:95:9d:80:37:c6:c0:7b:78:b5:07:3b:49:07:59:
                    ac:8d:b2:e8:43:27:db:9b:76:f3:12:fb:2c:54:6c:
                    c7:42:75:16:30:9e:8b:9f:b4:9b:e3:d2:37:9e:d5:
                    c8:44:c6:e9:90:09:1a:02:a0:91:f8:28:0c:70:81:
                    c7:3e:62:2c:0c:37:f2:d4:a9:2b:14:78:46:f5:65:
                    9e:c5:a0:3a:2e:e2:fd:e8:b1:ef:94:8d:e6:63:b4:
                    a9:95:64:55:c8:6d:71:66:ef:4a:c7:c2:c7:2a:d2:
                    a6:32:11:86:4e:cf:e6:9e:9c:41:cc:cd:2e:9b:20:
                    96:6d:b2:2b:bf:b5:5e:15:d3:1c:7f:ff:38:64:2b:
                    9b:86:d5:5a:1d:b0:22:76:2e:77:4b:95:3e:90:29:
                    aa:7a:6b:1e:f1:cc:e5:68:18:e3:ef:1e:9c:03:aa:
                    5d:af:b0:71:9d:89:36:ff:e3:4c:e1:3d:c3:f7:67:
                    8d:8e:40:dc:68:ce:99:80:76:7a:f9:ae:e1:56:9f:
                    55:d4:20:3a:91:3e:45:72:28:1c:cc:67:ae:74:11:
                    8e:02:d5:57:52:9a:1b:db:e7:e5:a5:0e:62:07:9a:
                    2d:ee:eb:4e:b5:6d:b5:77:36:39:a8:9e:b5:d1:31:
                    df:67:09:08:69:46:b5:d1:1d:27:17:db:b0:55:e6:
                    30:d7
                Exponent: 65537 (0x10001)
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        0a:a8:99:a2:4b:b6:61:01:6a:43:f8:79:e9:6a:84:66:d7:a1:
        62:e4:bb:89:ad:d7:7e:13:93:28:de:63:79:35:77:47:67:45:
        73:bc:1a:c6:ee:a1:0b:03:48:1d:d8:be:ac:55:1f:7c:9b:bf:
        be:cc:eb:55:bb:50:22:84:59:bf:71:f4:c7:47:bc:66:83:1f:
        76:0c:2c:e3:19:00:71:d9:90:ea:30:3b:31:d3:dd:fc:b0:4c:
        3c:59:b3:f6:f3:7d:37:f8:b5:bb:03:e1:39:30:6a:22:e6:3c:
        7d:7c:70:4a:89:69:aa:00:2f:da:a1:db:ee:03:dc:49:32:d0:
        7e:11:a0:70:2f:6d:c5:21:49:6d:00:1a:7b:69:4e:07:3e:4b:
        ac:f3:07:e3:07:c6:e4:d3:50:90:b9:c9:39:f3:d3:f5:a5:ca:
        87:47:9b:99:86:25:52:58:06:21:b5:36:06:a9:61:92:53:15:
        cb:20:c0:f2:65:3a:82:af:fe:d2:22:3a:eb:b7:9f:87:fb:40:
        52:fc:13:ec:49:5f:21:41:72:66:64:0a:ca:ab:87:95:48:25:
        e2:30:91:9f:78:c2:e8:82:63:5e:d2:fb:be:f2:7d:0f:e8:8d:
        0a:9e:af:cf:4d:a2:01:d5:bf:74:2a:13:11:82:62:d7:81:a2:
        ad:7a:57:d2
-----BEGIN CERTIFICATE-----
MIIDNjCCAh4CAwX1szANBgkqhkiG9w0BAQsFADBpMQswCQYDVQQGEwJSVTEMMAoG
A1UECAwDVWZhMQwwCgYDVQQHDANVZmExDDAKBgNVBAoMA3NsYjEMMAoGA1UEAwwD
c2xiMSIwIAYJKoZIhvcNAQkBFhNzdXBwb3J0QHNsYi5tZWR2LnJ1MB4XDTI0MDYy
NDEyMDAxOVoXDTI1MDYyNDEyMDAxOVowVzELMAkGA1UEBhMCUlUxDzANBgNVBAgM
Bk1vc2NvdzEPMA0GA1UEBwwGTW9zY293MQ0wCwYDVQQKDARUZXN0MRcwFQYDVQQD
DA50ZXN0QHRlc3QudGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
AJWdgDfGwHt4tQc7SQdZrI2y6EMn25t28xL7LFRsx0J1FjCei5+0m+PSN57VyETG
6ZAJGgKgkfgoDHCBxz5iLAw38tSpKxR4RvVlnsWgOi7i/eix75SN5mO0qZVkVcht
cWbvSsfCxyrSpjIRhk7P5p6cQczNLpsglm2yK7+1XhXTHH//OGQrm4bVWh2wInYu
d0uVPpApqnprHvHM5WgY4+8enAOqXa+wcZ2JNv/jTOE9w/dnjY5A3GjOmYB2evmu
4VafVdQgOpE+RXIoHMxnrnQRjgLVV1KaG9vn5aUOYgeaLe7rTrVttXc2OaietdEx
32cJCGlGtdEdJxfbsFXmMNcCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEACqiZoku2
YQFqQ/h56WqEZtehYuS7ia3XfhOTKN5jeTV3R2dFc7waxu6hCwNIHdi+rFUffJu/
vszrVbtQIoRZv3H0x0e8ZoMfdgws4xkAcdmQ6jA7MdPd/LBMPFmz9vN9N/i1uwPh
OTBqIuY8fXxwSolpqgAv2qHb7gPcSTLQfhGgcC9txSFJbQAae2lOBz5LrPMH4wfG
5NNQkLnJOfPT9aXKh0ebmYYlUlgGIbU2BqlhklMVyyDA8mU6gq/+0iI667efh/tA
UvwT7ElfIUFyZmQKyquHlUgl4jCRn3jC6IJjXtL7vvJ9D+iNCp6vz02iAdW/dCoT
EYJi14GirXpX0g==
-----END CERTIFICATE-----
"""

PRIVATE_KEY_CONTENT = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCVnYA3xsB7eLUH
O0kHWayNsuhDJ9ubdvMS+yxUbMdCdRYwnouftJvj0jee1chExumQCRoCoJH4KAxw
gcc+YiwMN/LUqSsUeEb1ZZ7FoDou4v3ose+UjeZjtKmVZFXIbXFm70rHwscq0qYy
EYZOz+aenEHMzS6bIJZtsiu/tV4V0xx//zhkK5uG1VodsCJ2LndLlT6QKap6ax7x
zOVoGOPvHpwDql2vsHGdiTb/40zhPcP3Z42OQNxozpmAdnr5ruFWn1XUIDqRPkVy
KBzMZ650EY4C1VdSmhvb5+WlDmIHmi3u6061bbV3NjmonrXRMd9nCQhpRrXRHScX
27BV5jDXAgMBAAECggEANml9+IsBdMYs/DDM+e3cifofa1EDFrK3a1dKw3d+Lka7
57m5aL88FKpezRbNy2mWBuqweXUhMSGLiJ1CM4dropP0bfAKOVsW32dyS0he8K9g
DXEtAxdqSyeopyrC4e4fmIJ9bVICsinDBKGH+YC1zEhiy9NxWDyNSN7L92BEE+ZR
FNlvDDTf9oripVY494uKc3rm5XPKmWVQwBRHSom625ajNtG0od6TrVsyrRMDWzKu
7cgM3F4AtkfrYa5tbMKnotYXG3gfihT53G0lsK6cHPS9lh+ja6PrWZJU1f7HTz9e
plsCgY/ZH53qAqxxQCzb3JN2pwpk0hJpP3e7S8+hqQKBgQDSaLXmCYI3pTQK475L
V10QDtOPBEOy9F7sWDPr7g4eXM8QnJPPldZCAXsHyaqHG9pq2fXfWc+hATtq0/Ph
f2Cb7TdaUtt7Fr/mVpWyZMODWV2HJ/uLUdKHkTmWqbtV58lBToTKadTt51S0XQNC
WyWX3tISW/aOV5DJmQB/zEEvDwKBgQC2CJZqFvPzVIJeZ+67pIjfAyv2E7qd4oP6
C7kQWIEAYmV374HL5ED4CwpuIMq+xszQvCTcehCxiJMNO0Rs91UXtcPWecN/z4MB
upPhaJwvUcBFUE8bUKOAUcXwarRfCX60gln+nCjDL4ECKol6Kt31qVtrCN8ORwQa
1wAQqKHhuQKBgQCxt1N7+qgLy/OLBxUhmaa2+27hKx7rNdA/G7ivG6C9MHKMe1O1
T79qfMmnqEPqXjI7ceFkRv1B5kKDVoZ0/hthWBkap0VOT8bCDHvf84/Xj1GZ6MFj
yTZi3tyfTrk2M9Ie4Ozz8jOwxWUb+jvYfhfgkIkqjJZRX9ChFiP/zUt5LQKBgChY
HOYkciri9wXvaQTjgYZT0KF4W+r0MiXwBTMvOmAYbr63MYA79X5EDCq+T9EahHha
ypym3R5L07OiCBdSdeSMX3wgfojMOA/hBzd1FPCT4NY751x5cdNVzFXtgE5z70YY
gdOhTpN76s7NGK0f5RO2VlGRpMYoTSuZrSUECuTZAoGAW/nxI9T1uQdbQqOHANRn
0nrJF6yK5EtSpQqgDMkpQR1Rm3v6DtsnS3kxzaBInjI+TLOVwoe5LtfvCP1CIfmO
WaoxaJ6exwhzMIYRnIOKaTo+kvcrcZODAqLzsicYlJI3swrK2DE5hkM8Y0//t7nx
PjChutV5gBYfDNiR8twClXY=
-----END PRIVATE KEY-----
"""