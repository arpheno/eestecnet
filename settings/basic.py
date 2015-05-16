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
    'mailqueue',
    'gunicorn',
    'sorl.thumbnail',
    'corsheaders',
    'rest_framework',
    'guardian',
)
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
