from django.db import models

from futily.utils.methods import normalize_unicode


class EaAsset(models.Model):
    ea_id = models.PositiveIntegerField()

    total_players = models.PositiveIntegerField(default=0)
    total_bronze = models.PositiveIntegerField(default=0)
    total_silver = models.PositiveIntegerField(default=0)
    total_gold = models.PositiveIntegerField(default=0)
    total_inform = models.PositiveIntegerField(default=0)
    total_special = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True

    def normalized_name(self):
        return normalize_unicode(self.name)

    def players(self):
        return self.player_set.all().prefetch_related('club', 'league', 'nation')


class AverageRatingModel(models.Model):
    average_rating = models.FloatField(default=0)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
