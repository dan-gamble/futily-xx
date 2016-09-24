from django.db import models

from cms.apps.pages.models import Page


class FooterLinkAbstract(models.Model):
    page = models.ForeignKey(
        Page,
        blank=True,
        null=True
    )

    link = models.CharField(
        max_length=1024,
        blank=True,
        null=True
    )

    link_text = models.CharField(
        max_length=512
    )

    target = models.CharField(
        max_length=128,
        choices=(
            ('_blank', 'New window'),
            ('_self', 'Same window')
        ),
        default='_self'
    )

    order = models.PositiveIntegerField(
        default='0'
    )

    def __unicode__(self):
        return self.link

    def __str__(self):
        return self.link

    def get_link(self):
        if self.page:
            return self.page.get_absolute_url()
        return self.link

    class Meta:
        ordering = ('order', 'pk', )
        abstract = True


class FooterLinkGroup(FooterLinkAbstract):

    def __unicode__(self):
        return self.link


class FooterLink(FooterLinkAbstract):

    group = models.ForeignKey(
        FooterLinkGroup,
        related_name='children',
    )

    def __unicode__(self):
        return self.link


class Footer(models.Model):

    header = models.CharField(
        max_length=2048
    )

    content = models.TextField()

    twitter_link = models.CharField(
        max_length=4096
    )

    linkedin_link = models.CharField(
        max_length=4096
    )

    email_link = models.CharField(
        max_length=4096
    )

    def __unicode__(self):
        return self.header
