from django.urls import path, include
from .views import BaseView


urlpatterns = [
    path("django/", include("django.contrib.admin.urls")),
    path("wagtail/", include("wagtail.admin.urls")),
    path("", BaseView.as_view(), name="base")
]
