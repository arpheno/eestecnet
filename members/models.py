from django.contrib.auth.models import User, Group, Permission
from django.db import models
from eestecnet import settings


class Member(models.Model):
    TYPE_CHOICES = (
        ('body', 'Body'),
        ('team', 'International Team'),
        ('commitment', 'Commitment'),
    )
    #General
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=15,
        choices=TYPE_CHOICES,
        default='commitment')
    thumbnail=models.ImageField(blank=True,null=True,upload_to="memberthumbs")
    #Members
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='members')
    priviledged = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='priviledged')
    def __unicode__(self):
        return self.name

    def member_count(self):
        return len(self.members.all())
class MemberImage(models.Model):
    property = models.ForeignKey(Member, related_name='images')
    image = models.ImageField(upload_to="memberimages")
