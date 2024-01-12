from django.db import models
from artist.models import Artist
from album.models import Album

# Create your models here.

class Song(models.Model): 
    deezer_id = models.IntegerField(unique=True, null=False)
    title = models.CharField(max_length=255, unique=True, null=False)
    release_date = models.DateField()
    preview = models.URLField(unique=True, null=False)
    song_artist = models.ManyToManyField(Artist)
    song_album = models.ManyToManyField(Album)