from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from blog_api.settings import ALLOWED_HOSTS
# Create your models here.

class Post (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique_for_date='creation_date')
    link = models.CharField(max_length=215)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')

    class Meta:
        ordering = ('-creation_date',)

    def get_absolute_url(self):
        url = reverse('blog_engine:show_post', kwargs={'post_id':str(self.id)})
        return url

    def __str__(self):
        return f"{self.id}). {self.title}"

class Upvote (models.Model):
    user = models.ForeignKey(User,
                             related_name='upvote',
                             on_delete=models.CASCADE)

    post = models.ForeignKey(Post,
                                    related_name='upvote',
                                    on_delete=models.CASCADE)
