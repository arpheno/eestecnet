import random
from django.forms import ModelForm
from django.forms import widgets
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, View
from events.models import Event, Application

def featuredevent():
    random_idx = random.randint(0, Event.objects.count() - 1)
    return Event.objects.all()[random_idx]

class InternationalEvents(ListView):
    model = Event
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(InternationalEvents, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['workshop_list'] = [event for event in Event.objects.filter(scope="international",category="workshop") for i in range(2)]
        context['exchange_list'] = [event for event in Event.objects.filter(scope="international",category="workshop") for i in range(2)]
        context['training_list'] = [event for event in Event.objects.filter(scope="international",category="workshop") for i in range(2)]
        context['other_list'] = [event for event in Event.objects.filter(scope="international",category="workshop") for i in range(2)]
        return context

class EventDetail(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    def get_context_data(self, **kwargs):
       # import pdb;pdb.set_trace()
        return super(EventDetail,self).get_context_data(**kwargs)

class ApplyForm(ModelForm):
    class Meta:
        model = Application
        fields=('letter','target','applicant')
        widgets = {
            'letter': widgets.Textarea(attrs={'rows':3,'cols':30,'placeholder':'Write a motivational Letter!'}),
            'target': widgets.HiddenInput(),
            'applicant': widgets.HiddenInput(),
            }


class ApplyToEvent(View):
    form_class = ApplyForm
    initial = {'key': 'value'}
    template_name = 'events/application_form.html'
    def get(self, request, *args, **kwargs):
        e = Event.objects.get(slug=kwargs['slug'])
        form = self.form_class(initial={'target':e.pk,'applicant':request.user})
        return render(request, self.template_name, {'form': form,'target':e.pk,'object':e})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse()

        return render(request, self.template_name, {'form': form})