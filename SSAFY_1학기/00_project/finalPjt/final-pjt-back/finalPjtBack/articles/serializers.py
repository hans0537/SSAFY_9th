from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

    
class CommentSerializer(serializers.ModelSerializer):
  class ArticletoComment(serializers.ModelSerializer):
    class Meta:
      model = Article
      fields = ('title',)
  article = ArticletoComment(read_only=True)
  class UsertoComment(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username',)
  user = UsertoComment(read_only=True)
  class Meta:
    model=Comment
    fields='__all__'
        
class ArticleSerializer(serializers.ModelSerializer):
  user = serializers.CharField(source='user.username',read_only=True)
  comment_set = CommentSerializer(many=True, read_only=True)
  comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
  class Meta:
    model=Article
    fields='__all__'
    
class CommentCreateSerializer(serializers.ModelSerializer):
    class ArticletoComment(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    article = ArticletoComment(read_only=True)
    class UsertoComment(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','username',)
    user = UsertoComment(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'