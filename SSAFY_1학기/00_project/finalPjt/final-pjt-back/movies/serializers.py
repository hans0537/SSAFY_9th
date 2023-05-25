from rest_framework import serializers
from .models import Movie,Review, Genre
from django.contrib.auth import get_user_model
import base64
from accounts.serializers import UserSerializer

        
class ReviewSerializers(serializers.ModelSerializer):
    class MoivetoReview(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = MoivetoReview(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        
class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializers(many=True,read_only=True)
    review_count = serializers.IntegerField(source="review_set.count",read_only=True)
    class Meta:
        model=Movie
        fields='__all__'
        
class ReviewcreateSerializers(serializers.ModelSerializer):
    class MoivetoReview(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = MoivetoReview(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        
class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'