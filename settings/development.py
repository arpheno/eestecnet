SECRET_KEY = 'o&)%bwhyl5(g)%rmq+knp%75y9s@j!a-x#3oh^rzuw$$=nld*x'
from basic import *
DEBUG = True
TEMPLATE_DEBUG = True


def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG={
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
CELERY_EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
COMPRESS_REBUILD_TIMEOUT=5

CORS_ORIGIN_ALLOW_ALL = True