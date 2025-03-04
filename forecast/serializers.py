from django.utils import timezone
from rest_framework import serializers

from forecast.models import CommodityForecaster


class CommodityForecasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommodityForecaster
        fields = ["id", "market", "commodity"]


class PredictionRequestSerializer(serializers.Serializer):
    markets = serializers.ListField()
    commodities = serializers.ListField()
    start_day = serializers.DateTimeField(default=timezone.now)
    days = serializers.IntegerField(default=3)
