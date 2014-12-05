from autoslug import AutoSlugField
from autoslug.utils import slugify
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.template.loader import render_to_string
from django.utils.datetime_safe import datetime
from gmapi.maps import Geocoder

from events.models import Event


TYPE_CHOICES = (
        ('body', 'Body'),
        ('team', 'International Team'),
        ('department', 'Board Department'),
        ('lc', 'Local Committee'),
        ('jlc', 'Junior Local Committee'),
        ('observer', 'Observer'),
    )


class Team(models.Model):
    """Member objects are used to unify and abstract away from the internal entity of parts of our organization.

    Members can be Observers, LCs, Junior LCs, International Teams or Bodies of the association.
    The goal using these objects is to unify the way how we handle interactions that are common to all five kinds of parts of eestec

    When Members are created first, a local event called Recruitment is automatically created. By applying to
    event, registered users can become part of one or more teams."""

    #General
    """ The name of the :class:`Member`"""
    name = models.CharField(max_length=50,unique=True)
    slug=AutoSlugField(populate_from='name')
    """The type of the :class:`Member`"""
    type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES,
        default='lc')
    thumbnail=models.ImageField(blank=True,null=True,upload_to="memberthumbs")
    thumbsource=models.CharField(max_length=100,blank=True,null=True)
    """The picture that should appear in the :class:`Member` list"""
    teamstub = models.TextField(blank=True, null=True)
    description= models.TextField(blank= True, null=True)
    """ LC info text"""
    facebook = models.URLField(blank=True, null=True)
    """ Facebook page for the member"""
    website = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    def board(self):
        return self.users.filter(membership__board=True)

    def normal_members(self):
        result = self.users.filter(membership__alumni=False)
        return result

    def alumni(self):
        result = self.users.filter(membership__alumni=True)
        return result

    def privileged(self):
        result = self.users.filter(membership__privileged=True)
        return result

    def as_html(self):
        return render_to_string('teams/team.html', {'object': self})

    def as_url(self):
        if self.is_lc():
            return reverse('cities:detail', kwargs={'slug': self.slug})
        return reverse('teams:detail', kwargs={'slug': self.slug})

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.thumbnail and not self.thumbsource:
            raise ValidationError('Please provide the source for the image')
    #Members
    users = models.ManyToManyField(
        'account.Eestecer', related_name='teams', through='news.Membership')
    founded = models.PositiveIntegerField(null=True, blank=True)
    """When the :class:`Member` was first established"""
    def save(self, *args,**kwargs):
        try:
            self.slug = slugify(self.name)
            geocoder = Geocoder()
            address = self.address
            results, status_code = geocoder.geocode({'address': self.name })
            self.lat, self.lng = results[0]['geometry']['location']['arg']
        except:
            pass
        if not self.pk:
            super(Team, self).save(*args, **kwargs)
            a = Event.objects.create(
                name=str(self.slug + " recruitment"),
                scope="local",
                category="recruitment",
                summary="Interested in joining? Apply here or click for more "
                        "information",
                description="We are always recruiting and welcoming new people.",
                start_date=datetime.now()
            )
            a.save()
            a.organizing_committee = [self]
        else:
            super(Team, self).save(*args, **kwargs)

    def __unicode__(self):
        if self.type not in ['jlc','lc','observer']:
            return self.name
        return self.type.upper() + " " + self.name
    def member_count(self):
        """ The amount of teams currently in the :class:`Member` """
        return len(self.users.all())

    def pending_applications(self):
        result = self.event_set.get(category='recruitment').applicants.all()
        return result

    def is_lc(self):
        return self.type in ['jlc', 'lc', 'observer']

    def last_event(self):
        try:
            return self.event_set.all().exclude(name='Recruitment').order_by('-start_date')[0].start_date
        except:
            return 0


class Board(models.Model):
    year = models.PositiveIntegerField()
    treasurer = models.OneToOneField("account.Eestecer",
                                     related_name="treasurer_in_board")
    vcia = models.OneToOneField("account.Eestecer", related_name="ia_in_board")
    vcea = models.OneToOneField("account.Eestecer", related_name="ea_in_board")
    vcpa = models.OneToOneField("account.Eestecer", related_name="pa_in_board")
    cp = models.OneToOneField("account.Eestecer", related_name="cp_in_board")


class MemberImage(models.Model):
    """ Helper class used to associate an arbitrary number of images with a
    :class:`Member` """

    property = models.ForeignKey(Team, related_name='images')
    image = models.ImageField(upload_to="memberimages")
    source = models.CharField(max_length=100,blank=True, null=True)

    def __unicode__(self):
        return render_to_string('teams/thumbnailed_image.html', {'object': self})

