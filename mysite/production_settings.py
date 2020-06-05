# Import all default settings.
from .settings import *

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}

# Static asset configuration.
# change STATIC_ROOT = 'staticfiles' to
STATIC_ROOT = '/app/mysite/trips/static'

# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers.
ALLOWED_HOSTS = ['*']

# Turn on DEBUG mode.
DEBUG = True

SITE_ID = 1