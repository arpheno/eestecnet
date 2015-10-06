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
ALLOWED_HOSTS = ['.eestec.net', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11212',
        }
}

CACHE_MIDDLEWARE_ALIAS="default"
CACHE_MIDDLEWARE_SECONDS=30
CACHE_MIDDLEWARE_KEY_PREFIX=""

EMAIL_HOST="localhost"
EMAIL_PORT = 25
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
os.environ['wsgi.url_scheme'] = 'https'
os.environ['HTTPS'] = "on"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
COMPRESS_ENABLED=True
COMPRESS_JS_FILTERS=["compressor.filters.closure.ClosureCompilerFilter"]
COMPRESS_CLOSURE_COMPILER_BINARY="/usr/bin/closure-compiler"
COMPRESS_CLOSURE_COMPILER_ARGUMENTS="--language_in ECMASCRIPT5"
COMPRESS_MINT_DELAY=100
