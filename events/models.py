import random
import sha

from autoslug import AutoSlugField
from autoslug.utils import slugify
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _





# Create your models here.
from django.db import models
from mailqueue.models import MailerMessage
from news.models import Membership


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
        ('recruitment','recruitment'),
)
class Event(models.Model):
    """Event objects encapsulate all information that is necessary to describe an event. """
    class Meta:
        verbose_name="Event"
        ordering=('name',)
        verbose_name_plural="Events"
    #General
    name = models.CharField(max_length=50,unique=True)
    """Name of the event. Examples: bEErSTEC, Trainers' Meeting, RISEX."""
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default='workshop')
    """Category of the event, for choices see :attr:`CATEGORY_CHOICES` ."""
    scope = models.CharField(max_length=15, choices=SCOPE_CHOICES, default='international')
    """Scope of the event, an event can be local or international.
    The main event list will only contain International Events by default. Also see
    :attr:`SCOPE_CHOICES`."""
    slug=AutoSlugField(populate_from='name')
    thumbnail=models.ImageField(upload_to='event_thumbnails')
    #Participants and Organizers
    max_participants = models.PositiveIntegerField(blank=True, null=True)
    """ Optional: Maximum amount of participants that will be admitted to the event """
    organizing_committee = models.ManyToManyField('teams.Team')
    """ Defines the Organizing Members of the event. May be more than one. Only
     those Members can be selected, the editor is a privileged member of."""
    participation_fee = models.PositiveIntegerField(default=0)

    def OC(self):
        """Helper function to display the names of organizing committees of an event"""
        return " ".join([c.name for c in self.organizing_committee.all()])

    organizers = models.ManyToManyField('account.Eestecer',
                                        related_name='events_organized')
    participants = models.ManyToManyField('account.Eestecer', related_name='events',
                                          through='Participation')
    applicants = models.ManyToManyField('account.Eestecer', related_name='applications',
                                        through='Application')

    def participant_count(self):
        """Number of participants"""
        return len(self.participants.all())

    #Time and place
    location = models.CharField(help_text=_("Where are you planning your Event?"), max_length=30, blank=True, null=True)
    """Optional: Location of the event."""
    start_date = models.DateField(help_text=_("When does your Event start?"))
    """Start of the event."""
    end_date = models.DateField(help_text=_("When does your Event end?"), null=True,
                                blank=True)
    """End of the event."""
    deadline = models.DateTimeField(help_text=_("Until when can participants apply?"),
                                    null=True, blank=True)
    """Deadline until no more applications will be accepted."""

    #Content
    summary = models.TextField()
    """ A summary of the event. This will be displayed on the events page."""
    description = models.TextField(help_text=_("Please provide a detailed description for interesed readers"))
    """ A detailed description of the event. Pictures and videos can be included here"""
    pax_report = models.TextField(blank=True, null=True)
    """ Optional: This is a field where the participants report can be stored and accessed."""
    organizer_report = models.TextField(blank=True, null=True)
    """ Optional: This is a field where the organizers report can be stored and accessed."""

    def as_html(self):
        return render_to_string('events/event.html', {'object': self})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super(Event, self).save(force_insert, force_update, using, update_fields)


    def clean(self):
        if self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError("The event may not begin after it ends.")
            if self.end_date < self.start_date:
                raise ValidationError("The event may not end before it starts.")
            if self.deadline.date() > self.end_date:
                raise ValidationError(
                    "The event deadline must be before the event ends.")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Participation(models.Model):
    class Meta:
        verbose_name="Participant"
        verbose_name_plural="Participants"

    participant = models.ForeignKey('account.Eestecer')
    """ The User issuing this application"""
    target = models.ForeignKey(Event)
    """ The :class:`Event` the User is applying for."""
    confirmed = models.BooleanField(default=False)
    confirmation = models.TextField(editable=False,null=True, blank=True)
    transportation = models.OneToOneField('Transportation',blank=True,null=True)
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        salt = sha.new(str(random.random())).hexdigest()[:5]
        self.confirmation = sha.new(salt+self.participant.get_full_name()).hexdigest()
        super(Participation,self).save()

    def __unicode__(self):
        return self.participant.get_full_name()

class Transportation(models.Model):
    arrival=models.DateTimeField()
    arrive_by=models.CharField(max_length=20,choices=[('plane','Plane'),
                                            ('bus','Bus'),
                                            ('train','Train'),
                                            ('car','Car'),
                                            ('other','other'),
                                            ('own','Own arrival')])
    arrival_number = models.CharField(_('Bus/Train/Plane Number'), max_length=30,
                                      blank=True, null=True)
    departure=models.DateTimeField(blank=True, null=True)
    depart_by=models.CharField(max_length=20,choices=[('plane','Plane'),
                                            ('bus','Bus'),
                                            ('train','Train'),
                                            ('car','Car'),
                                            ('other','other'),
                                            ('own', 'Own departure')], blank=True,
                               null=True)
    comment = models.TextField(blank=True, null=True)


class Application(models.Model):
    """Application objects link Users to :class:`Event` objects and provide additional information"""
    class Meta:
        unique_together=(('applicant','target'),)

    applicant = models.ForeignKey('account.Eestecer', editable=False)
    target = models.ForeignKey(Event, editable=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    letter = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    accepted = models.BooleanField(default=False)

    def member_in(self):
        """ returns a String containing all :class:`Member`s the applicant is part of """
        try:
            return ",".join(map(lambda c: c.name, self.applicant.teams.all()))
        except Exception, e:
            return "Error:%s" % str(e)

    def __unicode__(self):
        return self.applicant.get_full_name()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.target.category == "recruitment":
            if self.accepted:
                Membership.objects.create(
                    team=self.target.organizing_committee.all()[0],
                    user=self.applicant).save()
                self.delete()
            else:
                super(Application, self).save()
        else:
            if self.pk == None:
                pass
                #if timezone.now() > make_aware(self.target.deadline):#todo
                #   return
            if self.accepted:
                participation = Participation.objects.create(target=self.target,
                                                             participant=self.applicant)
                participation.save()
                message = MailerMessage()
                message.subject = "Congratulations! You were accepted to " + \
                                  participation.target.name
                message.content = "Dear " + participation.participant.first_name + \
                                  "\nPlease visit " + reverse(
                    'eventconfirmation', kwargs={
                    'slug': participation.target.slug}) + "to confirm your " \
                                                          "participation to the event" \
                                                          ".\n Thank you."
                message.from_address = "noreply@eestecnet",
                message.to_address = self.applicant.email
                message.save()

                self.delete()
            else:
                super(Application, self).save()


class IncomingApplication(Application):
    class Meta:
        proxy=True
class OutgoingApplication(Application):
    class Meta:
        proxy=True

class EventImage(models.Model):
    property = models.ForeignKey(Event, related_name='images')
    image = models.ImageField(upload_to="eventimages")

    def __unicode__(self):
        return render_to_string('teams/thumbnailed_image.html', {'object': self})
