"""
WSGI config for project Hobby Games.

"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.vagrant")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
