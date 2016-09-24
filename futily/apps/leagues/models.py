from django.core import urlresolvers
from django.db import models
from django.utils.text import slugify

from futily.apps.models import AverageRatingModel, EaAsset, TimeStampedModel
from ..nations.models import Nation


class League(EaAsset, TimeStampedModel, AverageRatingModel, models.Model):
    cached_url = models.CharField(max_length=1000, null=True, blank=True)

    name = models.CharField(max_length=100)
    name_abbr = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    nation = models.ForeignKey(Nation, blank=True, null=True)

    class Meta:
        ordering = ['-total_players', '-average_rating', 'name']
        verbose_name = 'League'
        verbose_name_plural = 'Leagues'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)

        super(League, self).save()

    def get_absolute_url(self, cached=False):
        if self.cached_url and cached:
            return self.cached_url

        url = urlresolvers.reverse('leagues:league', kwargs={'slug': self.slug})

        if url != self.cached_url:
            self.cached_url = url
            self.save()

        return url
