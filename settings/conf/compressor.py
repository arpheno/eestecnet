COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    ('text/x-sass', 'django_libsass.SassCompiler'),
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/ecmascript-6', 'babel --out-file {outfile} < {infile}'),
)
COMPRESS_ENABLED = True

