from autoslug import AutoSlugField
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.db import models
from django.template.loader import render_to_string

class Membership(models.Model):
    """Application objects link Users to :class:`Event` objects and provide additional
    information"""

    class Meta:
        permissions = (('view_membership', 'Can view membership'),)
        unique_together = (('user', 'team'),)

    user = models.ForeignKey('account.Eestecer')
    team = models.ForeignKey('teams.Team')
    date_joined = models.DateTimeField(auto_now_add=True)
    privileged = models.BooleanField(default=False)
    board = models.BooleanField(default=False)
    alumni = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.privileged:
            self.user.is_staff = True
            self.user.save()
            local, created = Group.objects.get_or_create(name='Local Admins')
            privileged, created = Group.objects.get_or_create(
                name=self.team.slug + "privileged")
            self.user.groups.add(local)
            self.user.groups.add(privileged)
        super(Membership, self).save()

    def email(self):
        return self.user.email
    def thumbnail(self):
        return self.user.thumbnail
    def __unicode__(self):
        return self.user.get_full_name()


class EntryManager(models.Manager):
    def get_queryset(self):
        return super(EntryManager, self).get_queryset().order_by('-pub_date')


class Entry(models.Model):
    class Meta:
        permissions = (('view_entry', 'Can view entry'),)
        verbose_name_plural = "entries"

    name = models.CharField(max_length=50, unique=True)
    author = models.ManyToManyField('teams.Team')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="entryimages")
    slug = AutoSlugField(populate_from='name')
    pub_date = models.DateTimeField(auto_now_add=True)
    objects = EntryManager()
    category = models.CharField(max_length=20, choices=(
    ("news", "EESTEC News"), ("carreer", "Carreer Offer")), default="news")
    published = models.BooleanField(default=False)
    front_page_news = models.BooleanField(default=False)

    def authors(self):
        return " ".join(str(a) for a in self.author.all())

    def as_html(self):
        return render_to_string('news/entry.html', {'object': self})

    def __unicode__(self):
        return self.name
    def clean(self):
        if not len(self.name.strip()):
            raise ValidationError("Headline may not be empty.")

# Create your models here.
