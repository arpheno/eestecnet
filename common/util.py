from django.core.urlresolvers import reverse_lazy


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Reversable(object):
    def get_absolute_url(self):
        return reverse_lazy(self._meta.model_name + '-detail', kwargs={'pk': self.pk})


def setup_view(view, request, *args, **kwargs):
    """Mimic as_view() returned callable, but returns view instance.

    args and kwargs are the same you would pass to ``reverse()``

    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view


