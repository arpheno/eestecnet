from autoslug import AutoSlugField
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100, unique=True)
    thumbnail = models.ImageField(upload_to='event_thumbnails')
    description = models.TextField()
    category = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    max_participants = models.PositiveIntegerField(blank=True, null=True)
    participation_fee = models.PositiveIntegerField(default=0)
    scope = models.CharField(max_length=15, default='international')
    location = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.DateField(help_text=_("When does your Event start?"))
    end_date = models.DateField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    pax_report = models.TextField(blank=True, null=True)
    organizer_report = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = "Event"
        ordering = ('name',)
        verbose_name_plural = "Events"


class Participation(models.Model):
    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"

    """ The User issuing this application"""
    target = models.ForeignKey(Event)
    """ The :class:`Event` the User is applying for."""
    confirmed = models.BooleanField(default=False)
    confirmation = models.TextField(editable=False, null=True, blank=True)
    transportation = models.OneToOneField('Transportation', blank=True, null=True)



class Transportation(models.Model):
    arrival = models.DateTimeField()
    arrive_by = models.CharField(max_length=20, choices=[('plane', 'Plane'),
                                                         ('bus', 'Bus'),
                                                         ('train', 'Train'),
                                                         ('car', 'Car'),
                                                         ('other', 'other'),
                                                         ('own', 'Own arrival')])
    arrival_number = models.CharField(_('Bus/Train/Plane Number'), max_length=30,
                                      blank=True, null=True)
    departure = models.DateTimeField(blank=True, null=True)
    depart_by = models.CharField(max_length=20, choices=[('plane', 'Plane'),
                                                         ('bus', 'Bus'),
                                                         ('train', 'Train'),
                                                         ('car', 'Car'),
                                                         ('other', 'other'),
                                                         ('own', 'Own departure')],
                                 blank=True,
                                 null=True)
    comment = models.TextField(blank=True, null=True)


class Application(models.Model):
    """Application objects link Users to :class:`Event` objects and provide additional
    information"""


    # target = models.ForeignKey(Event)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    letter = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    accepted = models.BooleanField(default=False)



class EventImage(models.Model):
    # property = models.ForeignKey(Event, related_name='images')
    image = models.ImageField(upload_to="eventimages")

    def __unicode__(self):
        return render_to_string('teams/thumbnailed_image.html', {'object': self})
