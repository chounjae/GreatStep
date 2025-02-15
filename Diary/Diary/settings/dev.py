from .base import *

DEBUG = True  # 개발에서는 True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']




# 개발용 SQLite 설정 유지
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # MySQL 엔진 설정
        'NAME': 'django_db',               # 데이터베이스 이름
        'USER': 'root',               # MySQL 사용자명
        'PASSWORD': '1234',       # MySQL 비밀번호
        'HOST': 'localhost',                  # MySQL 서버 주소 (로컬 서버 사용 시 'localhost')
        'PORT': '3306',                       # MySQL 포트 (기본값 3306)
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

###########################
INSTALLED_APPS += [
    'board',
    'Glogin',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE += [
    'allauth.account.middleware.AccountMiddleware',
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {"access_type": "online"},
    }
}

SOCIALACCOUNT_PROVIDERS["google"]["APP"] = {
    "client_id": config("client_id"),
    "secret": config("secret"),
    "key": "",
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

#로그 아웃시 리다이렉트 경로
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
#회원가입 후 리다이렉트 경로
ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/login/'
#로그인 후 리다이렉트 경로
LOGIN_REDIRECT_URL = 'http://localhost:8000/accounts/google/login/callback/'
#SMTP 정의
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



###########################