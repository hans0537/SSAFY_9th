from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleListSerializer(serializers.ModelSerializer):
    # comment_set =  serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # 특정 필드를 override 혹은 추가한 경우 read_only_fields에 넣는것이 아닌
    # 각각의 필드에 read_only를 넣는다.
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
   
    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = '__all__'
    
    def to_representation(self, instance):
        print(instance)
        rep = super().to_representation(instance)
        print(rep)
        rep['comments'] = rep.pop('comment_set', [])
        rep.pop('article', None)
        return rep