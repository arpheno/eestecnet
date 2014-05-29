from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from eestecnet import settings
from members.models import Member


class Event(models.Model):
    """Event objects encapsulate all information that is necessary to describe an event. """
    SCOPE_CHOICES = (
        ('local', 'Local'),
        ('international', 'International'),
    )
    CATEGORY_CHOICES = (
        ('ssa', 'Soft Skills Academy'),
        ('exchange', 'Exchange'),
        ('workshop', 'Workshop'),
        ('advanced_workshop', 'Advanced Skills Workshop'),
        ('exclusive_workshop', 'Exclusive Workshop'),
        ('operational', 'Operational Event'),
        ('congress', 'Congress'),
        ('ecm', 'EESTEC Chairpersons\' Meeting'),
        ('training', 'Training'),
    )
    #General
    name = models.CharField(max_length=50)
    """Name of the event. Examples: bEErSTEC, Trainers' Meeting, RISEX."""
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default='workshop')
    """Category of the event, for choices see :attr:`CATEGORY_CHOICES` ."""
    scope = models.CharField(max_length=15, choices=SCOPE_CHOICES, default='international')
    """Scope of the event, an event can be local or international.
    The main event list will only contain International Events by default. Also see
    :attr:`SCOPE_CHOICES`."""

    #Participants and Organizers
    max_participants = models.IntegerField(blank=True, null=True)
    """ Optional: Maximum amount of participants that will be admitted to the event """
    organizing_committee = models.ManyToManyField(Member)
    """ Defines the Organizing Members of the event. May be more than one. Only
     those Members can be selected, the editor is a priviledged member of."""
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='participants')
    """ A list of all Users currently connected to the event as participants.
    They are added by accepting applications"""
    organizers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='organizers')
    """ A list of all Users currently connected to the event as Organizers.
    Usually the head Organizers of the event."""
    participation_fee = models.PositiveIntegerField(blank=True, null=True)
    """Optional: Participation Fee for the event. """
    #Time and place
    location = models.CharField(max_length=30, blank=True, null=True)
    """Optional: Location of the event."""
    start_date = models.DateField()
    """Start of the event."""
    end_date = models.DateField(blank=True, null=True)
    """Optional: End of the event."""
    deadline = models.DateTimeField(blank=True, null=True)
    """Deadline until no more applications will be accepted."""

    #Content
    summary = models.TextField()
    """ A summary of the event. This will be displayed on the events page."""
    description = models.TextField()
    """ A detailed description of the event. Pictures and videos can be included here"""
    pax_report = models.TextField(blank=True, null=True)
    """ Optional: This is a field where the participants report can be stored and accessed."""
    organizer_report = models.TextField(blank=True, null=True)
    """ Optional: This is a field where the organizers report can be stored and accessed."""

    def participant_count(self):
        return str(len(self.participants.all()))

    def save(self, *args, **kwargs):
        """ We try to add all :class:`Application`s' respective users to :attr:`participants` ."""
        try:
            self.participants = [aplctn.applicant for aplctn in self.application_set.filter(accepted=True)]
        except:
            pass
        super(Event, self).save(*args, **kwargs)
        self.participants = [aplctn.applicant for aplctn in self.application_set.filter(accepted=True)]
        super(Event, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Application(models.Model):
    """Application objects link Users to :class:`Event` objects and provide additional information"""
    FOOD_CHOICES = (
        ('nopork', 'No Pork'),
        ('veggie', 'Vegetarian'),
        ('vegan', 'Vegan'),
    )
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL)
    """ The User issuing this application"""
    target = models.ForeignKey(Event)
    """ The :class:`Event` the User is applying for."""
    date = models.DateTimeField(auto_now_add=True)
    """ Auto: The date when the application is created. """
    letter = models.TextField(blank=True, null=True)
    """ Optional: Motivational letter, if the event requires one."""
    priority = models.IntegerField(blank=True, null=True)
    """Optional: Priority of the application as issued by the corresponding LC"""
    accepted = models.BooleanField(default=False)
    """If this field is set to true, the application is accepted and the User
    becomes a Participant of the :class:`Event`"""
    food_preferences = models.CharField(max_length=15, choices=FOOD_CHOICES, default='None')
    """ Food preferences as selected by the user """
    def member_in(self):
        """ returns a String containing all :class:`Member`s the applicant is part of """
        try:
            return ",".join(map(lambda c: c.name, self.applicant.members.all()))
        except Exception, e:
            return "Error:%s" % str(e)

    def __unicode__(self):
        return self.applicant.get_full_name()
