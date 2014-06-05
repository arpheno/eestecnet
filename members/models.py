from django.contrib.auth.models import User, Group, Permission
from django.db import models
from eestecnet import settings

class Member(models.Model):
    """Member objects are used to unify and abstract away from the internal entity of parts of our organization.
    Members can be Observers, LCs, Junior LCs, International Teams or Bodies of the association. The goal using these
    objects is to unify the way how we handle interactions that are common to all five kinds of parts of eestec
    When Members are created first, a local event called Recruitment is automatically created. By applying to that
     event, registered users can become part of one or more members."""
    TYPE_CHOICES = (
        ('body', 'Body'),
        ('team', 'International Team'),
        ('lc', 'Local Committee'),
        ('jlc', 'Junior Local Committee'),
        ('observer', 'Observer'),
    )
    #General
    name = models.CharField(max_length=50,unique=True)
    """ The name of the member"""
    type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES,
        default='lc')
    """The type of the member"""
    thumbnail=models.ImageField(blank=True,null=True,upload_to="memberthumbs")
    """The picture that should appear in the member list"""
    #Members
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='members')
    """ The people who are considered to be part of the member"""
    priviledged = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='priviledged')
    """The priviledged members of the member, usually persons on the board and OC"""
    #TODO should expire after a year
    founded=models.DateField(null=True, blank=True)
    """When the member was first established"""
    def __unicode__(self):
        return self.name
    def member_count(self):
        return len(self.members.all())
    def last_event(self):
        try:
            ownevents=self.event_set.all()
            if ownevents:
                return self.event_set.all().order_by('-start_date')[0].start_date
            else:
                return 0
        except:
            return 0

class MemberImage(models.Model):
    """ Helper class used to associate an arbitrary number of images with a :class:`Member` """

    property = models.ForeignKey(Member, related_name='images')
    image = models.ImageField(upload_to="memberimages")
    """An Image"""