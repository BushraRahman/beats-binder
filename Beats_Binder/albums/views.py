from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Album
from .search_form import SearchForm

# Create your views here.

class AlbumListView(ListView):
	model = Album
	
def search_results_view(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            search_input = form.cleaned_data["Search"]
            search_result = searchAPI(search_input)
            return render(request, "albums/search_results.html", context={"search_result": search_result["data"],
                                                                        	"search_input": search_input})
    else: 
        form = SearchForm()
    return render(request, "albums/search_results.html", 
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
