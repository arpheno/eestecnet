from django.db import models
from members.models import Member


class Entry(models.Model):
    author = models.ManyToManyField(Member)
    headline = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.message
# Create your models here.
