from .base import *

DEBUG = True  # 개발에서는 True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',  # 개발용 디버깅 툴 추가
]

MIDDLEWARE.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# 개발용 SQLite 설정 유지
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]
