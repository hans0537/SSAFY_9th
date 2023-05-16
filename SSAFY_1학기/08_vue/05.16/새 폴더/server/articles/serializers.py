from rest_framework import serializers
from .models import Articles

class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Articles
        # fields = ('id', 'title', 'content')
        fields = '__all__'
