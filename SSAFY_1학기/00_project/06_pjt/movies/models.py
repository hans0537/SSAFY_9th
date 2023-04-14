from django.db import models
from django.conf import settings

class Movie(models.Model):
    # 누가 적었는지 N:1 관계
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 좋아요 정보(user와 N:M)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    title = models.CharField(max_length=20)
    description = models.TextField()

    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

# 댓글 정보를 담을 클래스
class Comment(models.Model):
    # 누가 적었는지 N:1 관계
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 대댓글
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    # 어느 영화의 댓글인지
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content