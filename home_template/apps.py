from django.apps import AppConfig


class HomeAppConfig(AppConfig):
    default_auto_field = "django_mongodb_backend.fields.ObjectIdAutoField"
    name = "home"


    def ready(self):
        from . import telepath_adapters.bson_adapter
