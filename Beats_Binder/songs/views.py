from django.shortcuts import render, redirect
from song.models import Song
from django.http import HttpResponse
from django.contrib import messages
import datetime
import json

from django.shortcuts import render
from .models import Song

def list_view(request):
    songs = Song.objects.all()

    context = {
        'songs': songs,
    }

    return render(request, 'song_list.html', context)

