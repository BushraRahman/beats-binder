from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   #return HttpResponse("Hello, world. You're at the games index.")
   titlePage = "Games Index"
   gamesList = [{"name" : "Elder Scrolls: Oblivion", "Franchise" : True, "ethicallyAmbiguous" : False}, {"name" : "Furry Shades of Gray", "Franchise" : False, "ethicallyAmbiguous" : True}, {"name" : "Grand Theft Auto 6", "Franchise" : False, "ethicallyAmbiguous" : True}, {"name" : "Elden Ring", "Franchise" : True, "ethicallyAmbiguous" : False}, {"name" : "Minecraft", "Franchise" : True,  "ethicallyAmbiguous" : False}]
   return render(request, "games2/index.html", context = {'titlePage' : titlePage,
                                                         'gamesList' : gamesList})