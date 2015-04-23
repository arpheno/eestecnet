COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    ('text/x-sass', 'django_libsass.SassCompiler'),
    ('text/coffeescript', 'coffee --compile --stdio'),
)
COMPRESS_ENABLED = True
