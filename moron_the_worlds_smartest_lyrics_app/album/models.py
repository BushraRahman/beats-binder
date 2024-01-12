from django.db import models

# Create your models here.

class Album(models.Model): 
    deezer_id = models.IntegerField(unique=True, null=False)
    title = models.CharField(max_length=255, unique=True, null=False)
    release_date = models.DateField()
    cover = models.ImageField(unique=True, null=False)
    genre = models.IntegerField(unique=True, null=False)
    tracklist = models.URLField(unique=True, null=False)
    album_artist = models.ManyToManyField('artist.Artist')

def __str__(self):
    return self.name