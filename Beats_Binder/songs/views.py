from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Song
# Create your views here.

class SongListView(ListView):
	model = Song
	

# Create your views here.
def list_view(request):
    songs = Song.objects.all()

    context = {
        'songs': songs,
    }

    return render(request, 'song_list.html', context)
