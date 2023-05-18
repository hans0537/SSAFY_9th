from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
      like_articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)    
      like_movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
      followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
      class Meta:
        model=User
        fields=('id','username','email','profile','background','cho_points','groups','user_permissions','followings','followers', 'like_articles', 'like_movies')