from autoslug import AutoSlugField
from django.db import models

from members.models import Member


class Entry(models.Model):
    author = models.ManyToManyField(Member)
    """ The :class:`Members <members.models.Member>` authoring the news"""
    headline = models.CharField(max_length=50, unique=True)
    """ The headline"""
    slug = AutoSlugField(populate_from='headline')
    content = models.TextField()
    """The Content of the message"""
    pub_date = models.DateTimeField(auto_now_add=True)
    """ The publication date"""
    entry_image = models.ImageField(blank=True, null=True,upload_to="entryimages")
    """ Optionally, an image to add"""
    def __unicode__(self):
        return self.headline
# Create your models here.
