from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from eestecnet import settings
from members.models import Member


class Event(models.Model):

    """A Generic Event class, one of the basic classes

    .. note::

       An example of intersphinx is this: you **cannot** use :mod:`pickle` on this class.

    """
    SCOPE_CHOICES = (
        ('local', 'Local'),
        ('international', 'International'),
    )

    #General
    name = models.CharField(max_length=50)
    scope = models.CharField(
        max_length=15,
        choices=SCOPE_CHOICES,
        default='international')
    max_participants = models.IntegerField(blank=True, null=True)
    organizing_committee = models.ManyToManyField(Member)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True)

    #Time and place
    location = models.CharField(max_length=30,blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    deadline= models.DateTimeField(blank=True, null=True)

    #Content
    summary = models.TextField()
    description = models.TextField()
    pax_report = models.TextField(blank=True, null=True)
    organizer_report = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Application(models.Model):
    target = models.ForeignKey(Event)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL)
    date=models.DateTimeField(auto_now_add=True)
    letter = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
