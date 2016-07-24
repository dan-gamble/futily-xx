from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import NationViewset

router = routers.SimpleRouter()
router.register(r'nations', NationViewset)

urlpatterns = router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
