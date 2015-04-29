AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)
GUARDIAN_MONKEY_PATCH = False
ANONYMOUS_USER_ID = -1