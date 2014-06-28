from events.views import featuredevent


def random_event_processor(request):
    try:
        return {'featuredevent':featuredevent()}
    except:
        return {'None':None}