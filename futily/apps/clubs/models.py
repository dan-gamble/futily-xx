from django.core import urlresolvers
from django.db import models

from futily.apps.models import EaAsset, TimeStampedModel
from ..leagues.models import League


class Club(EaAsset, TimeStampedModel, models.Model):
    cached_url = models.CharField(max_length=1000, null=True, blank=True)

    name = models.CharField(max_length=100)
    name_abbr = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    league = models.ForeignKey(League, blank=True, null=True)

    image_dark_sm = models.CharField(max_length=255, blank=True, null=True)
    image_dark_md = models.CharField(max_length=255, blank=True, null=True)
    image_dark_lg = models.CharField(max_length=255, blank=True, null=True)

    image_normal_sm = models.CharField(max_length=255, blank=True, null=True)
    image_normal_md = models.CharField(max_length=255, blank=True, null=True)
    image_normal_lg = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    def __str__(self):
        return self.name

    def get_absolute_url(self, cached=False):
        if self.cached_url and cached:
            return self.cached_url

        url = urlresolvers.reverse('leagues:league', kwargs={'slug': self.slug})

        if url != self.cached_url:
            self.cached_url = url
            self.save()

        return url
