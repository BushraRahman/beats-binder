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
        addAlbumEntry(317522947,True)
        addAlbumEntry(10164620,True)
        addAlbumEntry(97412692,True)
        addAlbumEntry(106875912,True)
        addAlbumEntry(106710782,True)
        addSongEntry(2303246265,True)
        addSongEntry(2303246275,True)
        addSongEntry(2303246285,True)
        addSongEntry(2303246295,True)
        addSongEntry(2303246305,True)
        addSongEntry(89077521,True)
        addSongEntry(1682413517,True)
        addSongEntry(629561092,True)
        addSongEntry(4601933,True)
        addSongEntry(2603558,True)
        modifyAlbumSaved(447279465,True)
        modifyArtistSaved(14754433,False)
        modifySongSaved(2303246265,True)
        addAlbumEntry(106871722,False)

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
        print(" PSRT 3")
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
        cover = response["cover_medium"]
        genre = response["genres"]["data"][0]["name"]
        nb_tracks = response["nb_tracks"]
        duration = response["duration"]
        release_date = response["release_date"]
        record_type = response["record_type"]
        album = Album(deezer_id=deezerID,name=name,cover=cover,genre=genre,nb_tracks=nb_tracks,duration=duration,release_date=release_date,record_type=record_type,saved=saved)
        album.save()
        if not Artist.objects.filter(deezer_id = response["artist"]["id"]).exists():
            addArtistEntry(response["artist"]["id"],False)
        album.artist.add(Artist.objects.get(deezer_id = response["artist"]["id"]))
        print(response["contributors"][0]["id"])
        if (len(response["contributors"]) > 1):
            for i in range(1, len(response["contributors"])-1):
                if not Artist.objects.filter(deezer_id = response["contributors"][i]["id"]).exists():
                    addArtistEntry(response["contributors"][i]["id"],False)
                album.contributors.add(Artist.objects.get(deezer_id = response["contributors"][i]["id"]))

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
        song = Song(deezer_id=deezerID,name=name,duration=duration,preview=preview,saved=saved)
        song.save()
        if not Artist.objects.filter(deezer_id = response["artist"]["id"]).exists():
            addArtistEntry(response["artist"]["id"],False)
        song.artist.add(Artist.objects.get(deezer_id = response["artist"]["id"]))
        if not Album.objects.filter(deezer_id = response["album"]["id"]).exists():
            addAlbumEntry(response["album"]["id"],False)
        song.album.add(Album.objects.get(deezer_id = response["album"]["id"]))
        if (len(response["contributors"]) > 1):
            for i in range(1, len(response["contributors"])-1):
                if not Artist.objects.filter(deezer_id = response["contributors"][i]["id"]).exists():
                    addArtistEntry(response["contributors"][i]["id"],False)
                song.contributors.add(Artist.objects.get(deezer_id = response["contributors"][i]["id"]))

def modifyArtistSaved(deezerID, saved):
    addArtistEntry(deezerID, saved)
    artist = Artist.objects.get(deezer_id=deezerID)
    artist.saved = saved
    artist.save()

def modifyAlbumSaved(deezerID, saved):
    addAlbumEntry(deezerID, saved)
    album = Album.objects.get(deezer_id=deezerID)
    album.saved = saved
    album.save()

def modifySongSaved(deezerID, saved):
    addSongEntry(deezerID, saved)
    song = Song.objects.get(deezer_id=deezerID)
    song.saved = saved
    song.save()
        

