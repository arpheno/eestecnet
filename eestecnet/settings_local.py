import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = True
THUMBNAIL_DEBUG = True
SECRET_KEY = 'krrxqq_)5*4erfj0y9_sg=j(r3pfcr6b^2$&o8af#09mugi!*0'
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
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'eestecnet@gmail.com'
EMAIL_HOST_PASSWORD = 'eeStec4ever'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
