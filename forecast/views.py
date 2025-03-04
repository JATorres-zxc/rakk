from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from forecast.models import CommodityForecaster
from forecast.serializers import CommodityForecasterSerializer


class CommodityForecasterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CommodityForecaster.objects.all()
    serializer_class = CommodityForecasterSerializer

    def query_column(self, column):
        return (
            self
            .queryset
            .order_by(column)
            .distinct(column)
            .values_list(column, flat=True)
        )

    @action(detail=False, methods=["get"])
    def all_markets(self, request) -> Response:
        ms = self.query_column("market")
        return Response({"markets": list(ms)})

    @action(detail=False, methods=["get"])
    def all_commodities(self, request) -> Response:
        cs = self.query_column("commodity")
        return Response({"commodities": list(cs)})
