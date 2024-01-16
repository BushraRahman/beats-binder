from django.shortcuts import render
import requests
import json
import os
from artists.models import Artist
from albums.models import Album
from songs.models import Song

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

# Create your views here.

# for i in top_artists:
#     print(i)

def home_view(request):
    if request.method == 'POST' and 'run_script' in request.POST:
        addArtistEntry(14754433,True) 
    return render(request, 'home/home.html', 
                  context={'top_artists': top_artists,
                          'top_albums': top_albums,
                          'top_tracks': top_tracks})

def search_results_vew(request):
    return render(request, 'home/search_results.html')
    
def searchAPI():
    return render

def addSongEntry(deezerID, saved):
    url = "https://deezerdevs-deezer.p.rapidapi.com/track/" + str(deezerID)
    headers = {
    "X-RapidAPI-Key": "dc2e72cb1cmsh271df14842a824bp190aaajsnf4720429b177",
    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers).json()
    name = response["title"]
    duration = response["duraton"]
    preview = response["preview"]
    try: 
        artist = Artist.objects.get(deezer_id = response["artist"]["id"])
    except IntegrityError as error:
        addAlbumEntry(response["artist"]["id"], False)
        artist = Artist.objects.get(deezer_id = response["artist"]["id"])

def addArtistEntry(deezerID, saved):
    print("OMG IS THIS WORKING?")
    url = "https://deezerdevs-deezer.p.rapidapi.com/artist/" + str(deezerID)
    headers = {
    "X-RapidAPI-Key": "dc2e72cb1cmsh271df14842a824bp190aaajsnf4720429b177",
    "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers).json()
    name = response["name"]
    cover = response["picture_small"]
    nb_album = response["nb_album"]
    Artist.objects.create(deezer_id=deezerID,name=name,cover=cover,nb_album=nb_album,saved=saved).save()
