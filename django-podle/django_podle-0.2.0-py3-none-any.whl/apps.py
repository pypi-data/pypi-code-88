from django.apps import AppConfig


class PodleConfig(AppConfig):
    name = "podle"
    verbose_name = "Podle"

    def ready(self):
        import podle.signals.handlers  # noqa
