from rest_framework import serializers
from .models import Movie,Review
from django.contrib.auth import get_user_model

        
class ReviewSerializers(serializers.ModelSerializer):
    class MoivetoReview(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = MoivetoReview(read_only=True)
    class UsertoReview(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','username',)
    user = UsertoReview(read_only=True)
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
    class UsertoReview(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id','username',)
    user = UsertoReview(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'