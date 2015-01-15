import random
import sha

from autoslug import AutoSlugField
from autoslug.utils import slugify
from django.core.files import File
from django.core.urlresolvers import reverse
from django.db.models import ForeignKey
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mailqueue.models import MailerMessage

from apps.feedback.models import AnswerSet, Answer

from apps.news.models import Membership


SCOPE_CHOICES = (
    ('local', 'Local'),
    ('international', 'International'),
)
CATEGORY_CHOICES = (
    ('ssa', 'Soft Skills Academy'),
    ('exchange', 'Exchange'),
    ('workshop', 'Workshop'),
    ('operational', 'Operational Event'),
    ('training', 'Training'),
    ('imw', 'IMW'),
    ('recruitment', 'recruitment'),
)


class WorkshopManager(models.Manager):
    def get_queryset(self):
        return super(WorkshopManager, self).get_queryset().filter(category="workshop")


class TrainingManager(models.Manager):
    def get_queryset(self):
        return super(TrainingManager, self).get_queryset().filter(category="training")


class Event(models.Model):
    """Event objects encapsulate all information that is necessary to describe an
    event. """

    #General
    name = models.CharField(max_length=100, unique=True)
    thumbnail = models.ImageField(upload_to='event_thumbnails')
    description = models.TextField(
        help_text=_("Please provide a detailed description for interested readers"))
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES,
                                default='workshop')
    slug = AutoSlugField(populate_from='name')
    #People
    organizers = models.ManyToManyField(
        'account.Eestecer', related_name='events_organized')
    members = models.ManyToManyField(
        'account.Eestecer', related_name='events', through='Participation')
    def member_count(self):
        """Number of participants"""
        return len(self.members.all())
    applicants = models.ManyToManyField(
        'account.Eestecer', related_name='applications', through='Application')
    #Participants and Organizers
    max_participants = models.PositiveIntegerField(blank=True, null=True)
    organizing_committee = models.ManyToManyField('teams.Team')
    participation_fee = models.PositiveIntegerField(default=0)

    #Time and place
    scope = models.CharField(max_length=15, choices=SCOPE_CHOICES, default='international')
    location = models.CharField(help_text=_("Where are you planning your Event?"),
                                max_length=30, blank=True, null=True)
    """Start of the event."""
    start_date = models.DateField(help_text=_("When does your Event start?"))
    """End of the event."""
    end_date = models.DateField(help_text=_("When does your Event end?"), null=True,
                                blank=True)
    """Deadline until no more applications will be accepted."""
    deadline = models.DateTimeField(help_text=_("Until when can participants apply?"),
                                    null=True, blank=True)
    #Content
    """ A detailed description of the event. Pictures and videos can be included here"""
    pax_report = models.TextField(blank=True, null=True)
    """ Optional: This is a field where the participants report can be stored and
    accessed."""
    organizer_report = models.TextField(blank=True, null=True)
    """ Optional: This is a field where the organizers report can be stored and
    accessed."""
    feedbacksheet = ForeignKey('feedback.QuestionSet', null=True, blank=True)
    class Meta:
        verbose_name = "Event"
        ordering = ('name',)
        verbose_name_plural = "Events"
    def OC(self):
        """Helper function to display the names of organizing committees of an event"""
        return " ".join([c.name for c in self.organizing_committee.all()])


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        if (self.feedbacksheet):
            if self.pk:
                # if created
                orig = Event.objects.get(pk=self.pk)
                if orig.feedbacksheet != self.feedbacksheet:
                    #if feedbacksheet has changed
                    for pax in self.participation_set.all():
                        if pax.feedback:
                            pax.feedback.delete()
                        answers = AnswerSet.objects.create(parent=self.feedbacksheet)
                        answers.save()
                        pax.feedback = answers
                        pax.save()
                        for question in self.feedbacksheet.question_set.all():
                            Answer.objects.create(parent=pax.feedback, q=question).save()

        super(Event, self).save(force_insert, force_update, using, update_fields)

    def clean(self):
        if self.category == "training":
            if not self.thumbnail:
                if "ommunication" in self.name:
                    thumbname = "communication-skills.jpg"
                elif "motional" in self.name:
                    thumbname = "emotional-intelligence.jpg"
                elif "eedback" in self.name:
                    thumbname = "feedback.jpg"
                elif "resentation" in self.name:
                    thumbname = "presentation-skills.jpg"
                elif "rganizational" in self.name:
                    thumbname = "organizational-management.jpg"
                elif "eadership" in self.name:
                    thumbname = "leadership.jpg"
                elif "roject" in self.name:
                    thumbname = "project-management.jpg"
                elif "ime" in self.name and "anagement" in self.name:
                    thumbname = "time-management.jpg"
                elif "eambuilding" in self.name:
                    thumbname = "teambuilding.JPG"
                elif "acilitation" in self.name:
                    thumbname = "facilitation.jpg"
                elif "ynamics" in self.name:
                    thumbname = "group-dynamics.jpg"
                elif "ody" in self.name and "anguage" in self.name:
                    thumbname = "body-language.jpg"
                else:
                    thumbname = "trtlogo.png"
                with open('eestecnet/training/' + thumbname, 'rb') as doc_file:
                    self.thumbnail.save("thumbname.jpg", File(doc_file), save=True)
            if not str(self.start_date) in self.name:
                self.name = self.name + "-" + str(self.start_date)
        #if self.end_date:
        #    if self.start_date > self.end_date:
        #        raise ValidationError("The event may not begin after it ends.")
        #    if self.end_date < self.start_date:
        #        raise ValidationError("The event may not end before it starts.")
        #    if self.deadline:
        #        if self.deadline.date() > self.end_date:
        #            raise ValidationError(
        #                "The event deadline must be before the event ends.")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event', kwargs={'slug': self.slug})
    #TODO This isnt working right
    #workshops=WorkshopManager()
    #training=TrainingManager()
    #objects=models.Manager()


class Participation(models.Model):
    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"

    participant = models.ForeignKey('account.Eestecer')
    """ The User issuing this application"""
    target = models.ForeignKey(Event)
    """ The :class:`Event` the User is applying for."""
    confirmed = models.BooleanField(default=False)
    confirmation = models.TextField(editable=False, null=True, blank=True)
    transportation = models.OneToOneField('Transportation', blank=True, null=True)
    feedback = models.OneToOneField('feedback.AnswerSet', null=True, blank=True)
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        salt = sha.new(str(random.random())).hexdigest()[:5]
        self.confirmation = sha.new(salt + str(random.random())).hexdigest()
        super(Participation, self).save()

    def __unicode__(self):
        return self.participant.get_full_name()


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

    class Meta:
        unique_together = (('applicant', 'target'),)

    applicant = models.ForeignKey('account.Eestecer')
    target = models.ForeignKey(Event)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    letter = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    accepted = models.BooleanField(default=False)

    def outgoing(self):
        return [team for team in self.applicant.teams if team.is_lc][0]

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

        if not self.date:
            self.date = timezone.now()
        if self.target.deadline:
            if self.target.deadline < self.date:
                return
        if self.target.category == "recruitment":
            if self.accepted:
                membership, created = Membership.objects.get_or_create(
                    team=self.target.organizing_committee.all()[0],
                    user=self.applicant)
                membership.save()
                if not created:
                    self.delete()

            else:
                super(Application, self).save()
        else:
            if not self.pk:
                message = MailerMessage()
                message.subject = "Hey hey! Just dropping by to tell you that" + \
                                  self.request.user + " has applied to the event " + \
                                  self.target.name + "\n Please remember to send a " \
                                                     "priority list."
                message.from_address = "noreply@eestecnet",
                message.to_address = ", ".join(
                    user.email for user in self.applicant.lc.privileged)
                message.save()
            if self.accepted:
                participation, created = Participation.objects.get_or_create(
                    target=self.target,
                                                             participant=self.applicant)
                participation.save()
                message = MailerMessage()
                message.subject = "Congratulations! You were accepted to " + \
                                  participation.target.name
                message.content = "Dear " + participation.participant.first_name + \
                                  "\nPlease visit " + reverse(
                    'eventconfirmation', kwargs={
                        'slug': participation.target.slug}) + "to confirm your " \
                                                              "participation to the " \
                                                              "event" \
                                                              ".\n Thank you."
                message.from_address = "noreply@eestecnet",
                message.to_address = self.applicant.email
                message.save()

                self.delete()
            else:
                super(Application, self).save()


class IncomingApplication(Application):
    class Meta:
        proxy = True


class OutgoingApplication(Application):
    class Meta:
        proxy = True


class EventImage(models.Model):
    property = models.ForeignKey(Event, related_name='images')
    image = models.ImageField(upload_to="eventimages")

    def __unicode__(self):
        return render_to_string('teams/thumbnailed_image.html', {'object': self})
