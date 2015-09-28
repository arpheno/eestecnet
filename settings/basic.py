from settings.conf.debugtoolbar import *
from settings.conf.templates import TEMPLATE_DIRS

WSGI_APPLICATION = 'common.wsgi.application'
AUTH_USER_MODEL = 'accounts.Account'
ROOT_URLCONF = 'common.urls'
VERSION = 1
from conf.apps import *
# Third party apps
INSTALLED_APPS += (
    'compressor',
    # 'haystack',
    'kombu.transport.django',
    'djcelery',
    'gunicorn',
    'sorl.thumbnail',
    'corsheaders',
    'rest_framework',
    'guardian',
    'registration_api',
    'debug_toolbar',
    'django_statsd',
    'rest_framework_jwt',
)
INSTALLED_APPS += ("djcelery_email",)
# Own apps
INSTALLED_APPS += (
    'apps.questionnaires',
    'apps.prioritylists',
    'apps.accounts',
    'apps.announcements',
    'apps.events',
    'apps.teams',
    'common'
)
from conf.static import *

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

from conf.media import *
from conf.middleware import *
from conf.haystack import *
from conf.email import *
from conf.froala import *
from conf.compressor import *
from conf.localization import *
from conf.logging import *
from conf.mailqueue import *
from conf.rest import *
from conf.cors import *
from conf.authentication import *
from conf.statsd import *

AUTHENTICATION_BACKENDS

CORS_ORIGIN_WHITELIST
REST_FRAMEWORK
HAYSTACK_CONNECTIONS
COMPRESS_ENABLED
DEFAULT_FROM_EMAIL
FROALA_INCLUDE_JQUERY
TIME_ZONE
LOGGING
MAILQUEUE_CELERY
MEDIA_ROOT
MIDDLEWARE_CLASSES
TEMPLATE_DIRS
STATSD_MODEL_SIGNALS
DEBUG_TOOLBAR_PANELS

