from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   print("This is the games index...")
   titlePage = "Games Index"
   gamesList = [{"name" : "Elder Scrolls: Oblivion", "Franchise" : True, "ethicallyAmbiguous" : False}, {"name" : "Furry Shades of Gray", "Franchise" : False, "ethicallyAmbiguous" : True}, {"name" : "Grand Theft Auto 6", "Franchise" : False, "ethicallyAmbiguous" : True}, {"name" : "Elden Ring", "Franchise" : True, "ethicallyAmbiguous" : False}, {"name" : "Minecraft", "Franchise" : True,  "ethicallyAmbiguous" : False}]
   return render(request, "games/index.html", context = {'titlePage' : titlePage,
                                                         'gamesList' : gamesList})
   
def cookies(request):
   response = render(request, "games/cookies.html")
   response.set_cookie(key ="HI", value = "Bonjour")
   return response