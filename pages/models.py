from django.db import models


class Page(models.Model):
    url = models.CharField(max_length=30)
    content = models.TextField()
