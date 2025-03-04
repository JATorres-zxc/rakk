from rest_framework import serializers

from forecast.models import CommodityForecaster


class CommodityForecasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommodityForecaster
        fields = ["id", "market", "commodity"]
