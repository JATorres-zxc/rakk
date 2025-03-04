from django.urls import path
from rest_framework.routers import DefaultRouter

from forecast import views


router = DefaultRouter()
router.register("models", views.CommodityForecasterViewSet, basename="models")

urlpatterns = [
    path("predict/", views.get_predictions, name="predict"),
]
urlpatterns += router.urls
