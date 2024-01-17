from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Album
# Create your views here.

class AlbumListView(ListView):
	model = Album
	

# Create your views here.
