from django.shortcuts import render

#just displays the home page
def home(request):
    return render(request, "album/home_page.html")


# Create your views here.
