from django.urls import path

from . import views

app_name = "games2"

urlpatterns = [
   path("", views.index, name="index"),
]