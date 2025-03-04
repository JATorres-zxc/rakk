from rest_framework.routers import DefaultRouter

from forecast.views import CommodityForecasterViewSet


router = DefaultRouter()
router.register("models", CommodityForecasterViewSet, basename="models")

urlpatterns = router.urls
