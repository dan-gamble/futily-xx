from django.db import models


class EaAsset(models.Model):
    ea_id = models.PositiveIntegerField()

    total_players = models.PositiveIntegerField(default=0)
    total_bronze = models.PositiveIntegerField(default=0)
    total_silver = models.PositiveIntegerField(default=0)
    total_gold = models.PositiveIntegerField(default=0)
    total_informs = models.PositiveIntegerField(default=0)
    total_special = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
