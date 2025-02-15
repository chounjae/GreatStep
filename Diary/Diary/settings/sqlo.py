from .base import *

DEBUG = True  # 개발에서는 True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']




# 개발용 SQLite 설정 유지
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'db',  # docker-compose의 서비스 이름
        'PORT': '3306',
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]
