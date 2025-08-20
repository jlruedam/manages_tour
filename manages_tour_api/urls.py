from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, CityViewSet


router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'cities', CityViewSet)

urlpatterns = router.urls