from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from django.db import models
from account.models import Eestecer
from eestecnet import settings
from members.models import Member


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
class Event(models.Model):
    """Event objects encapsulate all information that is necessary to describe an event. """

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
    organizers = models.ManyToManyField(Eestecer, blank=True, null=True, related_name='organizers')
    """ A list of all Users currently connected to the event as Organizers.
    Usually the head Organizers of the event."""
    participation_fee = models.PositiveIntegerField(blank=True, null=True)
    """Optional: Participation Fee for the event. """
    participants=models.ManyToManyField(Eestecer, blank=True, null=True, related_name='participants')

    def participant_count(self):
        """Number of participants"""
        return len(self.participants.all())

    #Time and place
    location = models.CharField(help_text=_("Where are you planning your Event?"), max_length=30, blank=True, null=True)
    """Optional: Location of the event."""
    start_date = models.DateField(help_text=_("When does your Event start?"))
    """Start of the event."""
    end_date = models.DateField(blank=True, null=True,help_text=_("When does your Event end? (If ever ;) )"))
    """Optional: End of the event."""
    deadline = models.DateTimeField(blank=True, null=True,)
    """Deadline until no more applications will be accepted."""

    #Content
    summary = models.TextField(help_text=_("Please provide a short summary which will interest people in your Event."))
    """ A summary of the event. This will be displayed on the events page."""
    description = models.TextField(help_text=_("Please provide a detailed description for interesed readers"))
    """ A detailed description of the event. Pictures and videos can be included here"""
    pax_report = models.TextField(blank=True, null=True)
    """ Optional: This is a field where the participants report can be stored and accessed."""
    organizer_report = models.TextField(blank=True, null=True)
    """ Optional: This is a field where the organizers report can be stored and accessed."""


    def __unicode__(self):
        return self.name


class Application(models.Model):
    """Application objects link Users to :class:`Event` objects and provide additional information"""
    applicant = models.ForeignKey(Eestecer)
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
    def member_in(self):
        """ returns a String containing all :class:`Member`s the applicant is part of """
        try:
            return ",".join(map(lambda c: c.name, self.applicant.members.all()))
        except Exception, e:
            return "Error:%s" % str(e)

    def __unicode__(self):
        return self.applicant.get_full_name()

class EventImage(models.Model):
    property = models.ForeignKey(Event, related_name='images')
    image = models.ImageField(upload_to="eventimages")
