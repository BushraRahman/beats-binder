from django.shortcuts import render
import requests
import json
import os
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
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

    if request.method == 'POST' and 'run_script' in request.POST:
        addArtistEntry(1,True)
        addArtistEntry(14754433,True)
        addArtistEntry(12246,True)
        addAlbumEntry(447279465,True)
        addAlbumEntry(302068167,True)
        addSongEntry(2303246265,True)
        addSongEntry(2303246275,True)
        addSongEntry(2303246285,True)
        addSongEntry(2303246295,True)
        addSongEntry(2303246305,True)
        addSongEntry(89077521,True)
        addSongEntry(1682413517,True)

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

def addArtistEntry(deezerID, saved):
    if not Artist.objects.filter(deezer_id=deezerID).exists():
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

def addAlbumEntry(deezerID,saved):
    if not Album.objects.filter(deezer_id=deezerID).exists():
        url = "https://deezerdevs-deezer.p.rapidapi.com/album/" + str(deezerID)
        headers = {
            "X-RapidAPI-Key": "dc2e72cb1cmsh271df14842a824bp190aaajsnf4720429b177",
            "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers).json()
        name = response["title"]
        print(name)
        cover = response["cover_medium"]
        print(cover)
        genre = response["genres"]["data"][0]["name"]
        print(genre)
        nb_tracks = response["nb_tracks"]
        duration = response["duration"]
        release_date = response["release_date"]
        record_type = response["record_type"]
        print(record_type)
        album = Album(deezer_id=deezerID,name=name,cover=cover,genre=genre,nb_tracks=nb_tracks,duration=duration,release_date=release_date,record_type=record_type,saved=saved)
        album.save()
        album.artist.add(Artist.objects.get(deezer_id = 14754433))

def addSongEntry(deezerID, saved):
    if not Song.objects.filter(deezer_id=deezerID).exists():
        url = "https://deezerdevs-deezer.p.rapidapi.com/track/" + str(deezerID)
        headers = {
        "X-RapidAPI-Key": "dc2e72cb1cmsh271df14842a824bp190aaajsnf4720429b177",
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers).json()
        name = response["title"]
        duration = response["duration"]
        preview = response["preview"]
        song = Song(deezer_id=deezerID,name=name,duration=duration,preview=preview)
        song.save()
        song.album.add(Album.objects.get(deezer_id = 447279465))
        song.artist.add(Artist.objects.get(deezer_id = 14754433))

