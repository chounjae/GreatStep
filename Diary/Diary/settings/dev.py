from .base import *

DEBUG = False  # 개발에서는 True


ALLOWED_HOSTS = ['greatstep-production.up.railway.app', 'localhost', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = [
    'https://greatstep-production.up.railway.app',  # 배포된 URL
]
AUTH_USER_MODEL = 'board.User'   #user 를 어떻게 저장할건지 꼭 저장!

ACCOUNT_EMAIL_REQUIRED = False  
INTERNAL_IPS = [
    "127.0.0.1",
]
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
###########################
INSTALLED_APPS += [
    'useAPI',
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
LOGIN_REDIRECT_URL = 'http://greatstep-production.up.railway.app/board'
#SMTP 정의
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SOCIALACCOUNT_LOGIN_ON_GET = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # MySQL 사용
        'NAME': 'djangodb',  # 사용할 데이터베이스 이름
        'USER': os.getenv("MYSQL_PASSWORD"),  # MySQL 사용자
        'PASSWORD': '1234',  # 해당 사용자의 비밀번호
        'HOST': 'localhost',  # MySQL 서버 주소 (로컬이면 localhost)
        'PORT': '3306',  # MySQL 기본 포트
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
    }
}
