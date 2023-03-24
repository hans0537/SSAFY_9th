from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    MOVIE_CHOICES = (
		('comedy', '코미디'),
        ('thriller', '스릴러'),
        ('romance', '로맨스'),
        ('horror', '공포'),
    )
    genre = models.CharField(max_length=30, choices=MOVIE_CHOICES)
    # genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_img = models.ImageField(blank=True)
    poster_url = models.CharField(max_length=50)
    description = models.TextField()
    actor_image = models.ImageField(blank=True)