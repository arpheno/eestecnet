from django.shortcuts import render
from elfinder.views import ElfinderConnectorView
import logging
log = logging.getLogger(__name__)


def index(request):
    if request.is_ajax():
        return render(request, 'materials/elfinder-partial.html')
    return render(request, 'materials/elfinder.html')


def connector(request):
    connector_view = ElfinderConnectorView.as_view()
    log.debug(request.user.is_superuser)
    response = connector_view(request, optionset="default", start_path="default")
    return response
