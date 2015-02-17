import logging

logger = logging.getLogger(__name__)


class AdminMixin(object):
    def get_serializer(self, *args, **kwargs):
        serializer = super(AdminMixin, self).get_serializer(*args, **kwargs)
        return serializer

