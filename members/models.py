from autoslug import AutoSlugField
from django.contrib.auth.models import User, Group, Permission
from django.db import models
from account.models import Eestecer
from eestecnet import settings
TYPE_CHOICES = (
        ('body', 'Body'),
        ('team', 'International Team'),
        ('lc', 'Local Committee'),
        ('jlc', 'Junior Local Committee'),
        ('observer', 'Observer'),
    )
class Member(models.Model):
    """Member objects are used to unify and abstract away from the internal entity of parts of our organization.

    Members can be Observers, LCs, Junior LCs, International Teams or Bodies of the association.
    The goal using these objects is to unify the way how we handle interactions that are common to all five kinds of parts of eestec

    When Members are created first, a local event called Recruitment is automatically created. By applying to
    event, registered users can become part of one or more members."""

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
    """The picture that should appear in the :class:`Member` list"""
    description= models.TextField(blank= True, null=True)
    """ LC info text"""
    facebook = models.URLField(blank=True, null=True)
    """ Facebook page for the member"""
    #Members
    members = models.ManyToManyField(
        Eestecer,
        blank=True,
        null=True,
        related_name='members')
    """ The :class:`Users <account.models.Eestecer>` who are considered
    to be part of the :class:`Member`"""
    priviledged = models.ManyToManyField(
        Eestecer,
        blank=True,
        null=True,
        related_name='priviledged')
    """The priviledged :class:`Users <account.models.Eestecer>` of the :class:`Member`,
    they are able to make changes."""
    board = models.ManyToManyField(
        Eestecer,
        blank=True,
        null=True,
        related_name='board')
    """The board of the :class:`Member`"""
    founded=models.DateField(null=True, blank=True)
    """When the :class:`Member` was first established"""
    def __unicode__(self):
        if self.type not in ['jlc','lc','observer']:
            return self.name
        return self.type.upper() + " " + self.name
    def member_count(self):
        """ The amount of members currently in the :class:`Member` """
        return len(self.members.all()-1)
    def last_event(self):
        """  The date of the last :class:`~events.models.Event` organized by the :class:`Member` """
        try:
            return self.event_set.all().exclude(name='Recruitment').order_by('-start_date')[0].start_date
        except:
            return 0

class MemberImage(models.Model):
    """ Helper class used to associate an arbitrary number of images with a :class:`Member` """

    property = models.ForeignKey(Member, related_name='images')
    image = models.ImageField(upload_to="memberimages")
    """An Image"""