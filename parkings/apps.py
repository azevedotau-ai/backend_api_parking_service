from django.apps import AppConfig


class ParkingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parkings'

    def ready(self):
        import parkings.signals

