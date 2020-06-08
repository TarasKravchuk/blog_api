from django.urls import path
from .views import *

app_name = 'blog_engine'

urlpatterns = [
    path('main/', show_all_posts, name='all_posts'),
    path('main/<int:post_id>/', show_post, name='show_post'),
    path('add_new_post/', add_post, name='new_post'),
    path('<int:post_id>/delete/', delete_post, name='delete_post'),
    path('<int:post_id>/update/', update_post, name='update_post'),
    path('<int:post_id>/upvote/', add_upvote, name='post_upvote'),
    path('<int:post_id>/upvote/delete/', delete_upvote, name='post_upvote_delete'),
]
