from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    c = (('코미디','코미디'),('공포','공포'),('로맨스','로맨스'),('코미디 로맨스','코미디 로맨스'))
    genre = models.CharField(max_length=30, choices=c)
    score = models.FloatField()
    poster_url = models.CharField(max_length=50)
    description = models.TextField()
    actor_image = models.ImageField(blank=True, null=True)