"""
WSGI config for project Hobby Games, with low traffic.
uwsgi --virtualenv /path/to/virtualenv --http :9090 --gevent 100 --http-websockets --module wsgi
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.vagrant")

from django.core.wsgi import get_wsgi_application
from django.conf import settings
from dj_static import Cling
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer

_django_app = Cling(get_wsgi_application())
_websocket_app = uWSGIWebsocketServer()


def application(environ, start_response):
    if environ.get('PATH_INFO').startswith(settings.WEBSOCKET_URL):
        return _websocket_app(environ, start_response)
    return _django_app(environ, start_response)
