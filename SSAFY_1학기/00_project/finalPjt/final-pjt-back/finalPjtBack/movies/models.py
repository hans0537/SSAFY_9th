from django.db import models
from django.conf import settings


class Genre(models.Model):
  name=models.CharField(max_length=50)

class Movie(models.Model):
    adult = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=50,null=True)
    original_language = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    video = models.BooleanField(default=False)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genre_ids = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    
class Review(models.Model):
  movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
  content = models.CharField(max_length=100)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
