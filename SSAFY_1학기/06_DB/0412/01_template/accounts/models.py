from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # symetrical 대칭관계
    # 내가 너를 팔로우 했다고 너가 나를 팔로우 하는것을 방지
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
