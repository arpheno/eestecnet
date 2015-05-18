from autoslug import AutoSlugField
from django.contrib.auth.models import Group
from django.db import models

from apps.legacy.account.models import Eestecer
from apps.legacy.teams.models import Team


class Membership(models.Model):
    """Application objects link Users to :class:`Event` objects and provide additional
    information"""

    class Meta:
        unique_together = (('user', 'team'),)

    user = models.ForeignKey(Eestecer)
    team = models.ForeignKey(Team)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.privileged:
            self.user.is_staff = True
            self.user.save()
            local, created = Group.objects.get_or_create(name='Local Admins')
            self.user.groups.add(local)
        super(Membership, self).save()


class EntryManager(models.Manager):
    def get_queryset(self):
        return super(EntryManager, self).get_queryset().order_by('-pub_date')


class Entry(models.Model):
    class Meta:
        verbose_name_plural = "entries"

    name = models.CharField(max_length=50, unique=True)
    author = models.ManyToManyField(Team)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="entryimages")
    slug = AutoSlugField(populate_from='name')
    pub_date = models.DateTimeField(auto_now_add=True)
    objects = EntryManager()
    category = models.CharField(max_length=20, choices=(
        ("news", "EESTEC News"), ("carreer", "Carreer Offer")), default="news")
    published = models.BooleanField(default=False)
    front_page_news = models.BooleanField(default=False)

