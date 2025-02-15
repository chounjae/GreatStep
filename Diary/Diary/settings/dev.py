from .base import *

DEBUG = True  # 개발에서는 True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS += [
    'board',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',  # 로컬 개발용 MySQL DB
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]
