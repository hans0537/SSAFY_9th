from django.db import models

# Create your models here.
class Article(models.Model):    # models 상속
    title = models.CharField(max_length=20)  # 문자열 형태 CharField는 최대 몇자까지 명시를 해주어야 함
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at.month}/{self.created_at.day}에 생성된 {self.id}번글 - {self.title} : {self.content}'