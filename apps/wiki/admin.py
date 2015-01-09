from django.contrib import admin

# Register your models here.
from django.contrib.admin import TabularInline
from reversion import VersionAdmin
from apps.wiki.models import WikiPage, Reference, ExternalLink


class ExternalLinkInline(TabularInline):
    model = ExternalLink


class ReferenceInline(TabularInline):
    model = Reference


class WikiPageAdmin(VersionAdmin):
    inlines = [ExternalLinkInline, ReferenceInline]


admin.site.register(WikiPage, WikiPageAdmin)