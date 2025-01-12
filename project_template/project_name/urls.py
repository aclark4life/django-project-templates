from django.urls import path, include
from .views import BaseView


urlpatterns = [
    path("django/", include("django.admin.urls")),
    path("wagtail/", include("wagtail.admin.urls")),
    path("", BaseView.as_view(), name="base")
]
