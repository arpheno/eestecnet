from django.utils.http import urlquote_plus


def urlencode(query, doseq=0, safe=''):
    """Custom urlencode that leaves static map delimiters ("|", ",", ":") alone.

    Based on Django's unicode-safe version of urllib.quote_plus.

    """
    safe = safe + '|,:'
    if hasattr(query, 'items'):
        query = query.items()
    return '&'.join([urlquote_plus(k, safe) + '=' + urlquote_plus(v, safe)
                     for k, s in query
                     for v in ((isinstance(s, basestring) and [s])
                               or (doseq and hasattr(s, '__len__') and s)
                               or [s])])
