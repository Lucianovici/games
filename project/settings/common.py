# coding=utf-8
"""
Project's common settings.
"""
import os

DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', '3*@vw6*l^b86#28&9@6#)+5_mx$)m7leml!333(!1s!)@^d71^')

DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ws4redis',
    'landing',
    'chat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
                'django.core.context_processors.media',
                'ws4redis.context_processors.default',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(PROJECT_BASE_DIR, 'assets'),
    os.path.join(DJANGO_ROOT, 'chat/assets')
)

STATIC_ROOT = os.path.join(PROJECT_BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Websocket
WEBSOCKET_URL = '/ws/'

WS4REDIS_PREFIX = 'ws'

WS4REDIS_EXPIRE = 3600
