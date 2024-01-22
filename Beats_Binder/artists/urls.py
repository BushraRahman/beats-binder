from django.urls import path

from . import views

app_name = "artists"

urlpatterns = [
  # path("", views.ArtistListView.as_view(), name="list_view"),
  # path("/<int:pk>", views.ArtistDetailView.as_view(), name="detail_view"),
  path("search_results", views.search_results_view, name="search_results_view"),
  path("",views.ArtistList,name="list_view"),
  path("/<int:pk>",views.ArtistDetails,name="detail_view"),
]