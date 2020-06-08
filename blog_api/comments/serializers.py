from rest_framework.serializers import ModelSerializer
from .models import Comments

class CommentSerializerRead(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class CommentSerializerCreate(ModelSerializer):
    class Meta:
        model = Comments
        fields = ['content', 'author_name', 'related_post']

class CommentSerializerUpdate(ModelSerializer):
    class Meta:
        model = Comments
        fields = ['content']
