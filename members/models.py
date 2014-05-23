from django.contrib.auth.models import User
from django.db import models
from eestecnet import settings


class Member(models.Model):
    TYPE_CHOICES = (
        ('body', 'Body'),
        ('team', 'International Team'),
        ('commitment', 'Commitment'),
    )
    members = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, null=True, related_name='members')
    priviledged = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, null=True, related_name='priviledged')
    #General
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=15,
        choices=TYPE_CHOICES,
        default='commitment')
    def __unicode__(self):
        return self.name