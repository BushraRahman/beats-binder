from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Song
from .search_form import SearchForm
from home.views import modifySongSaved

# Create your views here.

class SongListView(ListView):
    model = Song
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm
        return context

class SongDetailView(DetailView):
	model = Song
	
def search_results_view(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            search_input = form.cleaned_data["Search"]
            search_result = searchAPI(search_input)
            return render(request, "songs/search_results.html", context={"search_result": search_result["data"],
                                                                         "search_input": search_input,
                                                                         "search_form": form})
    else: 
        form = SearchForm()
    return render(request, "songs/search_results.html", 
            context={'search_form': SearchForm})
    
def searchAPI(search_input):
    url = "https://deezerdevs-deezer.p.rapidapi.com/search/track"
    querystring = {"q": search_input}
    headers = {
        "X-RapidAPI-Key": "de8f6f2a3fmsh850207b34ede80bp17e3d8jsnd9883430d914",
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    search_results = response.json()
    return search_results

def SongList(request):
	object_list = Song.objects.all()
	print(object_list)
	#print(list(request.POST.keys())[1])
	if request.method == 'POST':
		modifySongSaved(list(request.POST.keys())[1])
	return render(request, "songs/song_list.html", context={"object_list": object_list})

def SongDetails(request, pk):
	artist = Song.objects.get(pk=pk)
	if request.method == 'POST':
		modifySongSaved(list(request.POST.keys())[1])
	return render(request, "songs/song_detail.html", context={"song": artist})