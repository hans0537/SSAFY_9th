from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model=User
      fields=('id','username','profile','background','cho_points','overview_points','followings')