from django.urls import path

from . import views

app_name = "games"

urlpatterns = [
   path("", views.index, name="index"),
   path('cookies/', views.cookies, name='cookies'),
   path('forms/', views.forms, name='forms'),
]