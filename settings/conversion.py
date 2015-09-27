try:
    from secret import DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER, SECRET_KEY
except:
    DATABASE_NAME = "myapp"
    DATABASE_PASSWORD = "dbpass"
    DATABASE_USER = DATABASE_NAME
    SECRET_KEY = "Lasjod"
from basic import *

INSTALLED_APPS
SECRET_KEY
DEBUG=True
ALLOWED_HOSTS = ['.eestec.net', 'localhost']
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': DATABASE_NAME,
#         'USER': DATABASE_USER,
#         'PASSWORD': DATABASE_PASSWORD,
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
CACHE_MIDDLEWARE_ALIAS="default"
CACHE_MIDDLEWARE_SECONDS=30
CACHE_MIDDLEWARE_KEY_PREFIX=""

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.DjangoFilterBackend'
    ],
}
EMAIL_HOST="localhost"
EMAIL_PORT = 25
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# os.environ['wsgi.url_scheme'] = 'https'
# os.environ['HTTPS'] = "on"
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
