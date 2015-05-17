# coding=utf-8
"""
Project settings for vagrant.
"""
try:
    from .common import *
except ImportError:
    pass

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS += ('192.168.33.111',)

# This directive is required during development and ignored in production environments.
# It overrides Django’s internal main loop and adds a URL dispatcher in front of the request handle.
WSGI_APPLICATION = 'ws4redis.django_runserver.application'

WS4REDIS_CONNECTION = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'password': None,
}
