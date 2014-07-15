import random

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms import ModelForm, TextInput
from django.forms import widgets
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, View
from events.models import Event, Application, Participation, Transportation

class HTML5Input(widgets.Input):
    def __init__(self, type, attrs):
        self.input_type = type
        super(HTML5Input, self).__init__(attrs)

def featuredevent():
    random_idx = random.randint(0, Event.objects.all().exclude(category='recruitment').count() - 1)
    return Event.objects.all().exclude(category='recruitment')[random_idx]

class InternationalEvents(ListView):
    model = Event
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(InternationalEvents, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        events=context['object_list'].filter(scope="international")
        context['active_list'] = []
        context['pending_list'] = []
        context['over_list'] = []
        for event in events:
            try:
                if event.deadline > timezone.now():
                    context['active_list'].append(event)
                if event.deadline < timezone.now() and event.end_date > timezone.now() \
                        .date():
                    context['pending_list'].append(event)
                if event.end_date < timezone.now().date():
                    context['over_list'].append(event)
            except:
                context['active_list'].append(event)
        return context

def confirm_event(request,slug):
    try:
        pa=Participation.objects.get(target__slug=slug,participant=request.user)
    except:
        return redirect(reverse('event',kwargs={'slug':slug}))
    pa.confirmed=True
    pa.confirmation=0
    pa.save()
    return redirect(reverse('event',kwargs={'slug':slug}))
class EventDetail(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    def get_context_data(self, **kwargs):

        context= super(EventDetail,self).get_context_data(**kwargs)
        try:
            context['participation']=Participation.objects.get(target__slug=self.kwargs['slug'],participant=self.request.user)
        except:
            context['participation']=None
        return context
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
            messages.add_message(
                self.request,
                messages.INFO,
                'Thank you for your application. You will be notified upon acceptance.')
            return redirect(reverse('event',kwargs={'slug':self.kwargs['slug']}))
        return render(request, self.template_name, {'form': form})
class TransportForm(ModelForm):
    class Meta:
        model = Transportation
        fields=('arrival','departure','arrive_by','depart_by','arrival_number')
        widgets = {
            'arrival': TextInput(attrs={'class': 'datetime'}),
            'departure': TextInput(attrs={'class': 'datetime'}),
        }

class FillInTransport(CreateView):
    form_class = TransportForm
    template_name = 'events/transportation_form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FillInTransport, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object'] = Event.objects.get(slug=self.kwargs['slug'])
        return context
    def post(self, request, *args, **kwargs):
        if not request.user.tshirt_size or not request.user.profile_picture:
            return redirect(reverse('event',kwargs={'slug':self.kwargs['slug']}))
        form = self.form_class(request.POST)
        pax=get_object_or_404(Participation,participant=request.user,target__slug=self.kwargs['slug'])
        trans=form.save()
        pax.transportation=trans
        pax.save()
        messages.add_message(
            self.request,
            messages.INFO,
            'Thank you for filling in your transportation details.')
        return redirect(reverse('event',kwargs={'slug':self.kwargs['slug']}))

