from django.db import models

class Album(models.Model):
	deezer_id = models.IntegerField()
	name = models.CharField(max_length=50)
	artist = models.ManyToManyField('artists.Artist')
	cover = models.URLField(max_length=200)
	genre = models.CharField(max_length=50)
	nb_tracks = models.IntegerField()
	duration = models.IntegerField()
	release_date = models.DateField()
	record_type = models.CharField(max_length=50)
	saved = models.BooleanField(default=False)
# Create your models here.
