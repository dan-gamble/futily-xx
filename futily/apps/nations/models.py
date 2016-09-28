from cms import externals, sitemaps
from cms.apps.pages.models import ContentBase, Page
from cms.models import SearchMetaBase, SearchMetaBaseSearchAdapter
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify

from futily.apps.models import AverageRatingModel, EaAsset, TimeStampedModel


class Nations(ContentBase):
    classifier = 'objects'
    urlconf = 'futily.apps.nations.urls'

    def __unicode__(self):
        return self.page.title


def get_default_nations_page():
    try:
        return Page.objects.filter(
            content_type=ContentType.objects.get_for_model(Nations),
        ).order_by('left')[0]
    except IndexError:
        return None


def get_default_nations_feed():
    page = get_default_nations_page()
    if page:
        return page.content
    return None


class Nation(SearchMetaBase, EaAsset, TimeStampedModel, AverageRatingModel, models.Model):
    page = models.ForeignKey(Nations, null=True, blank=False)

    cached_url = models.CharField(max_length=1000, null=True, blank=True)

    name = models.CharField(max_length=100)
    name_abbr = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    image = models.CharField(max_length=255, blank=True, null=True)

    image_sm = models.CharField(max_length=255, blank=True, null=True)
    image_md = models.CharField(max_length=255, blank=True, null=True)
    image_lg = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-total_players', '-average_rating', 'name']
        verbose_name = 'Nation'
        verbose_name_plural = 'Nations'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)

        super(Nation, self).save()

    def get_absolute_url(self):
        return self.page.page.reverse('nation_detail', kwargs={
            'slug': self.slug
        })

    def players(self):
        return self.player_set.all().prefetch_related('club', 'league', 'nation')


sitemaps.register(Nation)

externals.watson('register', Nation, adapter_cls=SearchMetaBaseSearchAdapter)
