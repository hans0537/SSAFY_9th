from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

class ActorSerializer(serializers.ModelSerializer):
    # 배우가 출연한 영화 필드를 가져온다
    movies = MovieListSerializer(many=True, read_only=True)

    # 요구사항에서 처럼 title만 가져오기 위해 필요 없는 필드 pop
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        for dic in rep['movies']:
            print(dic)
            dic.pop('overview')
        return rep
    
    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorListSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # 배우들의 id pop
        for dic in rep['actors']:
            dic.pop('id')

        return rep
    

    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # movie의 title만 뽑아주기 위해서
        rep['movie'].pop('overview')
        return rep
    
    class Meta:
        model = Review
        fields = '__all__'
