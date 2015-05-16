AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)
GUARDIAN_MONKEY_PATCH = False
GUARDIAN_GET_INIT_ANONYMOUS_USER = 'apps.accounts.factories.get_anonymous_user_instance'
ANONYMOUS_USER_ID = -1