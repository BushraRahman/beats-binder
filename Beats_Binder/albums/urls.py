from django.urls import path

from . import views

app_name = "albums"

urlpatterns = [
  #path("", views.home_view, name="home_view"),
  path("",views.AlbumListView.as_view(),name="list_view")
]