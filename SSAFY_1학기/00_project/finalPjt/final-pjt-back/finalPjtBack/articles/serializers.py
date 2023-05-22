from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model
import base64
from accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    class ArticletoComment(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    article = ArticletoComment(read_only=True)


    user = UserSerializer(read_only=True)

    class Meta:
        model=Comment
        fields='__all__'

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    like_cnt = serializers.IntegerField(source="like_users.count", read_only=True)

    image_base64 = serializers.SerializerMethodField()

    def get_image_base64(self, article):
        if article.image:
            with open(article.image.path, 'rb') as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                return encoded_string
        return None
    
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
        
    class parentComment(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content')
    parent_comment = parentComment(read_only=True)

class CoCommentCreateSerializer(serializers.ModelSerializer):
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

    class parentComment(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content')
    parent_comment = parentComment(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'