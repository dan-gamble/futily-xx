from cms import externals, sitemaps
from cms.apps.pages.models import ContentBase
from cms.models import SearchMetaBase, SearchMetaBaseSearchAdapter
from django.db import models
from django.utils.text import slugify

from futily.apps.models import AverageRatingModel, EaAsset, TimeStampedModel
from ..nations.models import Nation


class Leagues(ContentBase):
    classifier = 'objects'
    urlconf = 'futily.apps.leagues.urls'

    def __unicode__(self):
        return self.page.title


class League(SearchMetaBase, EaAsset, TimeStampedModel, AverageRatingModel, models.Model):
    page = models.ForeignKey(Leagues, null=True, blank=False)

    cached_url = models.CharField(max_length=1000, null=True, blank=True)

    name = models.CharField(max_length=100)
    name_abbr = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    nation = models.ForeignKey(Nation, blank=True, null=True)

    class Meta:
        ordering = ['-total_players', '-average_rating', 'name']
        verbose_name = 'League'
        verbose_name_plural = 'Leagues'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)

        super(League, self).save()

    def get_absolute_url(self):
        return self.page.page.reverse('league_detail', kwargs={
            'slug': self.slug
        })

    def clubs(self):
        return self.club_set.all()


sitemaps.register(League)

externals.watson('register', League, adapter_cls=SearchMetaBaseSearchAdapter)
