STATSD_MODEL_SIGNALS = True
STATSD_CLIENT = 'django_statsd.clients.normal'
STATSD_PATCHES = [
    'django_statsd.patches.db',
    'django_statsd.patches.cache',
]
TOOLBAR_STATSD = {
    'graphite': 'http://localhost:8005',
    'roots': {
        'timers': ['stats.timers.views.get.count', 'stats.timers.views.post.count'],
        'counts': ['stats.response.200', 'stats.response.400']
    }
}
