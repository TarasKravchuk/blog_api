from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'title', 'link', 'author_name']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
