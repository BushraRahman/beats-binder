from django.urls import path

from . import views

app_name = "songs"

urlpatterns = [
  path("", views.SongListView.as_view(), name="list_view"),
  path("/<int:pk>", views.SongDetailView.as_view(), name="list_view"),
  path("/song_search_results", views.search_results_view, name="search_results_view"),
]