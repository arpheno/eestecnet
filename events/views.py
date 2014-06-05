from django.forms import ModelForm
from django.forms import widgets
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, View
from events.models import Event, Application


class InternationalEvents(ListView):
    model = Event
    def get_queryset(self):
        return Event.objects.filter(scope="international")

class EventDetail(DetailView):
    model = Event

class ApplyForm(ModelForm):
    class Meta:
        model = Application
        fields=('letter','target','applicant')
        widgets = {
            'letter': widgets.TextInput(
                attrs={"placeholder": "Optional: Motivational Letter?"}),
            'target': widgets.HiddenInput(),
            'applicant': widgets.HiddenInput(),
            }


class ApplyToEvent(View):
    form_class = ApplyForm
    initial = {'key': 'value'}
    template_name = 'events/application_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={'target':kwargs['pk'],'applicant':request.user})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse()

        return render(request, self.template_name, {'form': form})