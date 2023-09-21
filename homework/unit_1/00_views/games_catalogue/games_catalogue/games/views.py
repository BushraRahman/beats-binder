from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   #return HttpResponse("Hello, world. You're at the games index.")
   titlePage = "Games Index"
   gamesList = [{"name" : "Furry Shades of Gray", "Franchise" : False}, {"name" : "Among Us", "Franchise" : False}, {"name" : "Elden Ring", "Franchise" : True}, {"name" : "Minecraft", "Franchise" : True}]
   return render(request, "games/index.html", context = {'titlePage' : titlePage,
                                                         'gamesList' : gamesList})