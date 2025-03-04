from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.request import Request

from forecast.models import CommodityForecaster
from forecast.serializers import (
    CommodityForecasterSerializer, PredictionRequestSerializer
)
from forecast.ml.predict import predict_best_day


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

    @action(detail=False)
    def all_markets(self, request):
        ms = self.query_column("market")
        return Response({"markets": list(ms)})

    @action(detail=False)
    def all_commodities(self, request):
        cs = self.query_column("commodity")
        return Response({"commodities": list(cs)})


@api_view(["get"])
def get_predictions(request: Request) -> Request:
    queries = PredictionRequestSerializer(data=request.GET)
    if not queries.is_valid():
        return Response(
            {
                "message": "Some query params are required.",
                "errors": queries.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    queries = queries.validated_data

    entries = CommodityForecaster.objects.filter(
        market__in=queries["markets"], commodity__in=queries["commodities"],
    )

    predictions = []

    for forecaster in entries:
        prediction = predict_best_day(
            forecaster.market,
            forecaster.commodity,
            forecaster.load_model(),
            queries["start_day"],
            queries["days"],
        )
        predictions.append(prediction)

    return Response({"predictions": predictions})
