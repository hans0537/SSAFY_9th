from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
    
class ArticleListSerializer(serializers.ModelSerializer):
    author = UserSerializer(source="user", read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'author')
        read_only_fields = ('user', )