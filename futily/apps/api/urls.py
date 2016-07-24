from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ClubViewset, LeagueViewset, NationViewset

router = routers.SimpleRouter()
router.register(r'nations', NationViewset)
router.register(r'leagues', LeagueViewset)
router.register(r'clubs', ClubViewset)

urlpatterns = router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
