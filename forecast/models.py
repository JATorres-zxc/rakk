from pathlib import Path

import keras
from django.db import models

import forecast


def trained_models_cache_path():
    return Path(forecast.__file__) / "ml/trained_models"


class CommodityForecaster(models.Model):
    market = models.CharField(max_length=255)
    commodity = models.CharField(max_length=255)
    path = models.FilePathField(path=trained_models_cache_path)
    trained_on = models.DateTimeField()

    def __str__(self) -> str:
        return f"<Forecaster for {self.market}'s {self.commodity}>"

    def load_model(self) -> keras.Model:
        return keras.models.load_model(self.path)
