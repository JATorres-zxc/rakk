from django.contrib import admin

from forecast.models import CommodityForecaster


@admin.register(CommodityForecaster)
class CommodityForecasterAdmin(admin.ModelAdmin):
    pass
