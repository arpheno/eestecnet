from autoslug import AutoSlugField
from django.core.urlresolvers import reverse
from django.db import models
from django.template.loader import render_to_string


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

    # other stuff
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






class MemberImage(models.Model):
    """ Helper class used to associate an arbitrary number of images with a
    :class:`Member` """

    property = models.ForeignKey(Team, related_name='images')
    image = models.ImageField(upload_to="memberimages")
    source = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return render_to_string('teams/thumbnailed_image.html', {'object': self})

