STATSD_MODEL_SIGNALS = True
STATSD_CLIENT = 'django_statsd.clients.toolbar'
STATSD_PATCHES = [
    'django_statsd.patches.db',
    'django_statsd.patches.cache',
]
