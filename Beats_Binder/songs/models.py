from django.db import models

class Song(models.Model):
	deezer_id = models.IntegerField()
	name = models.CharField(max_length=100)
	duration = models.IntegerField()
	preview = models.URLField(max_length=200)
	saved = models.BooleanField(default=False)
# Create your models here.
