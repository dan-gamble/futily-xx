from cms.apps.pages.models import ContentBase


class Builder(ContentBase):
    def __unicode__(self):
        return self.page.title
