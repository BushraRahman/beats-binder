from django.db import models

class Song(models.Model):
	deezer_id = models.IntegerField()
	name = models.CharField(max_length=100)
	albums = models.ManyToManyField('albums.Album')
	artists = models.ManyToManyField('artists.Artist')
	duration = models.IntegerField()
	preview = models.URLField(max_length=200)
# Create your models here.
