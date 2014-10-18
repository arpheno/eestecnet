from django.db import models


class Page(models.Model):
    url = models.CharField(max_length=30)
    content = models.TextField()

    def __unicode__(self):
        return self.url


class Stub(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField()
    content = models.TextField(max_length=140)
    image = models.ImageField(upload_to="stubs")
    group = models.CharField(max_length=20)