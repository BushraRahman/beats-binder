from django.db import models
from album.models import Album

# Create your models here.

class Song(models.Model): 
    deezer_id = models.IntegerField(unique=True, null=False)
    title = models.CharField(max_length=255, unique=True, null=False)
    release_date = models.DateField()
    preview = models.URLField(unique=True, null=False)
    song_artist = models.ManyToManyField('artist.Artist')
    song_featured = models.ManyToManyField('artist.Artist', related_name='featured')
    song_album = models.ManyToManyField(Album)

def __str__(self):
    return self.name