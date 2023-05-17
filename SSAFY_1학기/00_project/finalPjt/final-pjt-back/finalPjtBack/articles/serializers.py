from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
  user = serializers.CharField(source='user.username',read_only=True)
  class Meta:
    model=Article
    fields='__all__'
    
class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Comment
    fields='__all__'