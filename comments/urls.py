from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
    path('<int:post_id>/', show_post_comments, name='post_comments'),
    path('<int:post_id>/add/', add_comment, name='add_comment'),
    path('<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('<int:comment_id>/update/', update_comment, name='update_comment'),
    ]