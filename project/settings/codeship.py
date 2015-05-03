try:
    from .common import *
except ImportError:
    pass

# Configure Codeship Postgres DB for test.
# https://codeship.com/documentation/databases/postgresql/

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': os.environ.get('PG_USER'),
        'PASSWORD': os.environ.get('PG_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5433',  # For Postgres 9.3
    }
}