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
    'registration_api',
    'debug_toolbar',
    'django_statsd',
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
STATSD_MODEL_SIGNALS = True
STATSD_CLIENT = 'django_statsd.clients.toolbar'
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'django_statsd.panel.StatsdPanel',
]
STATSD_PATCHES = [
    'django_statsd.patches.db',
    'django_statsd.patches.cache',
]

