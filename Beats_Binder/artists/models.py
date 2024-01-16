from django.db import models

class Artist(models.Model):
	deezer_id = models.IntegerField()
	name = models.CharField(max_length=100)
	cover = models.URLField(max_length=200)
	albums = models.ManyToManyField('albums.Album')
	songs = models.ManyToManyField('songs.Song')
	nb_album = models.IntegerField
	saved = models.BooleanField(default=False)
# Create your models here.

# Create your models here.
