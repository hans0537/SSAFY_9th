from rest_framework import serializers
from .models import User
from movies.models import Movie
from articles.models import Article
import base64

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    followings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    followers_cnt = serializers.IntegerField(source='followers.count', read_only=True)
    followings_cnt = serializers.IntegerField(source='followings.count', read_only=True)
    
    like_articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)    
    like_movies = MovieSerializer(many=True, read_only=True)
    worldcup_movies = MovieSerializer(many=True, read_only=True)

    articles = ArticleSerializer(many=True, read_only=True, source='article_set')

    image_base64 = serializers.SerializerMethodField()

    def get_image_base64(self, user):
        if user.profile:
            with open(user.profile.path, 'rb') as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                return encoded_string
        return None
    

    class Meta:
      model=User
      fields=('id','username','email','profile','background','cho_points','overview_points','groups','user_permissions','followings','followers', 'like_articles', 'like_movies', 'worldcup_movies', 'articles', 'followers_cnt', 'followings_cnt', 'image_base64')

class FriendListSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    followings = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['followers', 'followings',]

    def get_followers(self, obj):
        return UserSerializer(obj.followers.all(), many=True).data

    def get_followings(self, obj):
        return UserSerializer(obj.followings.all(), many=True).data
