"""
Project settings applied for heroku instance.
"""
import dj_database_url

try:
    from .common import *
except ImportError:
    pass

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SSLIFY_DISABLE = False

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)