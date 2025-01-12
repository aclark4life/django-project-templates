from django.urls import path, include
from django.contrib import admin
from .views import BaseView


urlpatterns = [
    path("django/", admin.site.urls),
    path("wagtail/", include("wagtail.admin.urls")),
    path("", BaseView.as_view(), name="base")
]
