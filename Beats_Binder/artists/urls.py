from django.urls import path
from .views import ArtistListView, search_artist

urlpatterns = [
    path('', ArtistListView.as_view(), name='artist_list'),
    path('search/', search_artist, name='search_artist'),
]
