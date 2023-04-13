from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = '__all__'
        # 원하는 부분의 데이터만 넘기고 싶으면
        fields = ('id', 'title', 'content',)

