from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
   print("This is the games index...")
   titlePage = "Games Index"
   gamesList = [{"name" : "Elder Scrolls: Oblivion", "Franchise" : True, "ethicallyAmbiguous" : False}, {"name" : "Furry Shades of Gray", "Franchise" : False, "ethicallyAmbiguous" : True}, {"name" : "Grand Theft Auto 6", "Franchise" : False, "ethicallyAmbiguous" : True}, {"name" : "Elden Ring", "Franchise" : True, "ethicallyAmbiguous" : False}, {"name" : "Minecraft", "Franchise" : True,  "ethicallyAmbiguous" : False}]
   return render(request, "games/index.html", context = {'titlePage' : titlePage,
                                                         'gamesList' : gamesList})
   
# def cookies(request):
#    response = render(request, "games/cookies.html")
#    response.set_cookie(key ="HI", value = "Bonjour")
#    return response

def cookies(request):
   dico_cookies = request.COOKIES
   visit_nbr = 0
   if 'visit_nbr' in dico_cookies:
       try:
           visit_nbr = int(dico_cookies['visit_nbr']) + 1
       except:
           visit_nbr = 1
   else:
       visit_nbr = 1
   response = render(request, "games/cookies.html",
                     context={'visit_nbr': visit_nbr})
   response.set_cookie(key="visit_nbr", value=visit_nbr,
max_age=datetime.timedelta(seconds=10))
   #  expires=datetime.datetime(2023, 10, 2, 18, 23))
   return response

def forms(request):
    return render(request, "games/forms.html")