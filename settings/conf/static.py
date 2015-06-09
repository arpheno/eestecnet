import os

from BASE_DIR import BASE_DIR

STATIC_ROOT = os.path.join(BASE_DIR, 'serve', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'bower_components')]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
