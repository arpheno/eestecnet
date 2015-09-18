COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    ('text/x-sass', 'django_libsass.SassCompiler'),
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/ecmascript-6', 'babel --out-file {outfile} < {infile}'),
)
COMPRESS_ENABLED = False
COMPRESS_JS_FILTERS=["compressor.filters.closure.ClosureCompilerFilter"]
COMPRESS_CLOSURE_COMPILER_BINARY="/usr/bin/closure-compiler"
COMPRESS_CLOSURE_COMPILER_ARGUMENTS="--language_in ECMASCRIPT5"
COMPRESS_MINT_DELAY=100
