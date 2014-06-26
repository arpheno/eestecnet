from events.views import featuredevent


def random_event_processor(request):
   return {'featuredevent':featuredevent()}