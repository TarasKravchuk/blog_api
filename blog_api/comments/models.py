from django.db import models
from django.contrib.auth.models import User
from blog_engine.models import Post
# Create your models here.

class Comments (models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_name')
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='related_post')
    content = models.CharField (max_length=200)

    def __str__(self):
        return f"{str(self.id)}). {self.content}"
