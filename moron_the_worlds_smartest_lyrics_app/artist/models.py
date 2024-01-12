from django.db import models
from song.models import Song
from album.models import Album

# Create your models here.

class Artist(models.Model): 
    deezer_id = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=255, unique=True, null=False)
    link = models.URLField(max_length=255, unique=True, null=False)
    image = models.ImageField(unique=True, null=False)
    top_albums = models.ManyToManyField(Album)
    top_songs = models.ManyToManyField(Song)
    
def __str__(self):
    return self.name