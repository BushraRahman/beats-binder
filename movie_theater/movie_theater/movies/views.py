from django.shortcuts import render

from django.http import HttpResponse

def index(request):
   return HttpResponse("Hello, world. You're at the movies index.")

Let’s create the movies/urls.py and add these lines:

from django.urls import path

from . import views

app_name = "movies"

urlpatterns = [
   path("", views.index, name="index"),
]

Let’s edit these lines in movie_theater/urls.py:

from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('movies/', include('movies.urls', namespace='movies')),
] 

