from autoslug import AutoSlugField
from autoslug.utils import slugify
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse
from django.db import models
from django.template.loader import render_to_string
from django.utils.datetime_safe import datetime
from guardian.shortcuts import assign_perm

from apps.gmapi.maps import Geocoder
from apps.events.models import Event


TYPE_CHOICES = (
    ('body', 'Body'),
    ('team', 'International Team'),
    ('department', 'Board Department'),
    ('lc', 'Local Committee'),
    ('jlc', 'Junior Local Committee'),
    ('observer', 'Observer'),
)


class Team(models.Model):
    """ When Members are created first, a local event called Recruitment is automatically
     created. By applying to event, registered users can become part of one or more
     teams."""
    # General
    name = models.CharField(max_length=50, unique=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="memberthumbs")
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(blank=True, null=True)
    # People
    users = models.ManyToManyField(
        'account.Eestecer', related_name='teams', through='news.Membership')
    def organizers(self):
        return self.users.filter(membership__board=True)
    def privileged(self):
        return self.users.filter(membership__privileged=True)
    def members(self):
        return self.users.filter(membership__alumni=False)
    def alumni(self):
        return self.users.filter(membership__alumni=True)
    def member_count(self):
        """ The amount of teams currently in the :class:`Member` """
        return len(self.users.all())
    #other stuff
    category = models.CharField(max_length=30, choices=TYPE_CHOICES, default='lc')
    thumbsource = models.CharField(max_length=100, blank=True, null=True)
    teamstub = models.TextField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    founded = models.PositiveIntegerField(null=True, blank=True)

    def get_absolute_url(self):
        if self.is_lc():
            return reverse('cities:detail', kwargs={'slug': self.slug})
        return reverse('teams:detail', kwargs={'slug': self.slug})

    #Members

    def save(self, *args, **kwargs):
        try:
            self.slug = slugify(self.name)
            geocoder = Geocoder()
            address = self.address
            results, status_code = geocoder.geocode({'address': self.name})
            self.lat, self.lng = results[0]['geometry']['location']['arg']
        except:
            pass

        super(Team, self).save(*args, **kwargs)
        privileged, created = Group.objects.get_or_create(name=self.slug + "_privileged")
        privileged.save()
        privileged.user_set = self.privileged()
        privileged.save()
        assign_perm('change_team', privileged, self)
        if not self.pk:
            a = Event.objects.create(
                name=str(self.slug + " recruitment"),
                scope="local",
                category="recruitment",
                description="We are always recruiting and welcoming new people.",
                start_date=datetime.now()
            )
            a.save()
            a.organizing_committee = [self]

    def __unicode__(self):
        if self.category not in ['jlc', 'lc', 'observer']:
            return self.name
        return self.category.upper() + " " + self.name

    def pending_applications(self):
        result = self.event_set.get(category='recruitment').applicants.all()
        return result

    def is_lc(self):
        return self.category in ['jlc', 'lc', 'observer']

    def last_event(self):
        try:
            return \
                self.event_set.all().exclude(category='recruitment').order_by('-start_date')[
                    0].start_date
        except:
            return 0


class Board(models.Model):
    year = models.PositiveIntegerField()
    treasurer = models.OneToOneField("account.Eestecer",
                                     related_name="treasurer_in_board",
                                     null=True, blank=True)
    vcia = models.OneToOneField("account.Eestecer", related_name="ia_in_board",
                                null=True, blank=True)
    vcea = models.OneToOneField("account.Eestecer", related_name="ea_in_board",
                                null=True, blank=True)
    vcpa = models.OneToOneField("account.Eestecer", related_name="pa_in_board",
                                null=True, blank=True)
    cp = models.OneToOneField("account.Eestecer", related_name="cp_in_board",
                              null=True, blank=True)


class MemberImage(models.Model):
    """ Helper class used to associate an arbitrary number of images with a
    :class:`Member` """

    property = models.ForeignKey(Team, related_name='images')
    image = models.ImageField(upload_to="memberimages")
    source = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return render_to_string('teams/thumbnailed_image.html', {'object': self})

