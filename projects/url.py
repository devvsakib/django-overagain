from django.urls import path
from . import views


urlpatterns = [
    path("", views.projects),
    path("dynamic/<str:test>", views.dynamic),
]
