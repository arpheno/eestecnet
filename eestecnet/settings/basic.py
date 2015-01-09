WSGI_APPLICATION = 'eestecnet.wsgi.application'
AUTH_USER_MODEL = 'account.Eestecer'
ROOT_URLCONF = 'eestecnet.urls'
VERSION = 1
from conf.apps import *

INSTALLED_APPS += (
    'compressor',
    'haystack',
    'kombu.transport.django',
    'djcelery',
    'mailqueue',
    'froala_editor',
    'gunicorn',
    'sorl.thumbnail',
    'form_utils',
    'reversion',
)
# Own apps
INSTALLED_APPS += (
    'apps.teams',
    'apps.events',
    'apps.account',
    'apps.statistics',
    'apps.gmapi',
    'apps.password_reset',
    'apps.news',
    'apps.elfinder',
    'apps.wiki',
    'apps.pages',
)
from conf.templates import *
TEMPLATE_CONTEXT_PROCESSORS += (
    'eestecnet.context_processors.random_event_processor',
    'eestecnet.context_processors.my_feedback',
    'eestecnet.context_processors.login_processor',
    'eestecnet.context_processors.date_now',
    'eestecnet.context_processors.my_search',
)
from conf.static import *

STATICFILES_FINDERS +=(
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

HAYSTACK_CONNECTIONS
COMPRESS_ENABLED
DEFAULT_FROM_EMAIL
FROALA_INCLUDE_JQUERY
TIME_ZONE
LOGGING
MAILQUEUE_CELERY
MEDIA_ROOT
MIDDLEWARE_CLASSES
