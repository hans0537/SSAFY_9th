from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile = models.ImageField(blank=True)
    background = models.ImageField(blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    # 초성 퀴즈 포인트 정보
    cho_points = models.IntegerField(default=0)
    # 줄거리 퀴즈 포인트 정보
    overview_points = models.IntegerField(default=0)