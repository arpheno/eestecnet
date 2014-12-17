from autoslug import AutoSlugField

# Create your models here.
from django.db.models import Model, CharField, DateTimeField, URLField, IntegerField, \
    ForeignKey
from froala_editor.fields import FroalaField


class ExternalLink(Model):
    url = URLField()
    comment = CharField(max_length=255)
    page = ForeignKey('wiki.WikiPage')


class Reference(Model):
    number = IntegerField()
    source = CharField(max_length=255)
    page = ForeignKey('wiki.WikiPage')


class WikiPage(Model):
    name = CharField(max_length=50)
    content = FroalaField(options={'height': 600})
    last_modified = DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="name")
