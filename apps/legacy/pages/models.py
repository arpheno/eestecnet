from django.db import models


class Page(models.Model):
    url = models.CharField(max_length=30)
    content = models.TextField()

    def __unicode__(self):
        return self.url


class Stub(models.Model):
    def __unicode__(self):
        return self.group + " - " + self.name

    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    description = models.TextField(max_length=140)
    image = models.ImageField(upload_to="stubs")
    group = models.CharField(max_length=20)


class WebsiteFeedback(models.Model):
    def __unicode__(self):
        return str(self.date)

    email = models.EmailField(null=True, blank=True)
    date = models.DateTimeField(auto_created=True, editable=False, auto_now_add=True)
    subject = models.TextField(default="")
    content = models.TextField()
    user = models.ForeignKey('account.Eestecer', editable=False, blank=True, null=True)
    read = models.BooleanField(default=False)


class WebsiteFeedbackImage(models.Model):
    image = models.ImageField(upload_to="userfeedback")
    entity = models.ForeignKey('pages.WebsiteFeedback')