from django.shortcuts import render
import requests
import json
import os
from artists.models import Artist
from albums.models import Album
from songs.models import Song

# Create your views here.

from .search_form import SearchForm

def home_view(request):
    absolute_path = os.path.dirname(os.path.abspath(__file__))

    artists_data = open(absolute_path + '/json/top_artists.json')
    top_artists = json.load(artists_data)
    artists_data.close()

    albums_data = open(absolute_path + '/json/top_albums.json')
    top_albums = json.load(albums_data)
    albums_data.close()

    tracks_data = open(absolute_path + '/json/top_tracks.json')
    top_tracks = json.load(tracks_data)
    tracks_data.close()
    
    return render(request, 'home/home.html', 
                  context={'top_artists': top_artists,
                          'top_albums': top_albums,
                          'top_tracks': top_tracks,
                          'search_form': SearchForm})

def search_results_view(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_box = form.cleaned_data["search_box"]
            search_result = searchAPI(search_box[0])
            return render(request, "home/search_results.html", context={"search_results": search_results})
    else: 
        form = SearchForm()
    return render(request, "home/search_results.html", 
            context={'search_form': SearchForm})
    
def searchAPI(search_input):
    url = "https://deezerdevs-deezer.p.rapidapi.com/search"
    querystring = {"q": search_input}
    headers = {
        "X-RapidAPI-Key": "de8f6f2a3fmsh850207b34ede80bp17e3d8jsnd9883430d914",
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    search_results = response.json()
    return search_results

# def addSongEntry(deezerID, saved):
#     url = "https://deezerdevs-deezer.p.rapidapi.com/track/" + str(deezerID)
#     headers = {
#     "X-RapidAPI-Key": "dc2e72cb1cmsh271df14842a824bp190aaajsnf4720429b177",
#     "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
#     }
#     response = requests.get(url, headers=headers).json()
#     name = response["title"]
#     duration = response["duraton"]
#     preview = response["preview"]
#     try: 
#         artist = Artist.objects.get(deezer_id = response["artist"]["id"])
#     except IntegrityError as error:
#         addAlbumEntry(response["artist"]["id"], False)
#         artist = Artist.objects.get(deezer_id = response["artist"]["id"])

# def addArtistEntry(deezerID, saved):
#     for x in Artist.objects.all().iterator():
#         x.delete() 
#     url = "https://deezerdevs-deezer.p.rapidapi.com/artist/" + str(deezerID)
#     headers = {
#     "X-RapidAPI-Key": "dc2e72cb1cmsh271df14842a824bp190aaajsnf4720429b177",
#     "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
#     }
#     response = requests.get(url, headers=headers).json()
#     name = response["name"]
#     cover = response["picture_small"]
#     nb_album = response["nb_album"]
#     Artist.objects.create(deezer_id=deezerID,name=name,cover=cover,nb_album=nb_album,saved=saved).save()
