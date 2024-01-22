from django.urls import path

from . import views

app_name = "songs"

urlpatterns = [
<<<<<<< HEAD
  path("", views.SongListView.as_view(), name="list_view"),
  path("/<int:pk>", views.SongDetailView.as_view(), name="list_view"),
  path("/song_search_results", views.search_results_view, name="search_results_view"),
=======
  # path("", views.SongListView.as_view(), name="list_view"),
  # path("/<int:pk>", views.SongDetailView.as_view(), name="list_view"),
  path("search_results", views.search_results_view, name="search_results_view"),
  path("",views.SongList,name="list_view"),
  path("/<int:pk>",views.SongDetails,name="detail_view"),
>>>>>>> 5904e9c076aca88dcb926abeff4a81e60edb9469
]