import os

from django.apps import AppConfig


class ForecastConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forecast'

    def ready(self):
        os.environ["KERAS_BACKEND"] = "torch"
