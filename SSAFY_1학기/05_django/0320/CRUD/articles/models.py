from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # DB에 집접적인 변경이 아님으로 migrate안해도 됨
    def __str__(self):
        return f'{self.pk}번째글 : {self.title}'