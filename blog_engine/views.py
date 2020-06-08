import json
from rest_framework import status
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from .serializers import *
from .models import Post, Upvote
# Create your views here.

@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny])
def show_all_posts (request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({'posts': serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny])
def show_post (request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(post)
    return JsonResponse({'post': serializer.data}, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_post(request):
    data = json.loads(request.body)
    author_name = request.user
    new_post = Post.objects.create(title=data['title'], author_name=author_name,)
    new_post.link = new_post.get_absolute_url()
    new_post.save()
    serializer = PostSerializer(new_post)
    return JsonResponse({'new_post': serializer.data}, status=status.HTTP_200_OK)

@transaction.non_atomic_requests
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_post(request, post_id):
    post = get_object_or_404(Post, author_name=request.user, id=post_id)
    post.delete()
    return JsonResponse({f'Post {post.title}': 'successfully deleted'}, status=status.HTTP_200_OK)

@transaction.non_atomic_requests
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_post(request, post_id):
    post = get_object_or_404(Post, author_name=request.user, id=post_id)
    data = json.loads(request.body)
    post.title = data['title']
    post.link = post.get_absolute_url()
    post.save()
    serializer = PostSerializer(post)
    return JsonResponse({'new_post': serializer.data}, status=status.HTTP_200_OK)

@transaction.non_atomic_requests
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_upvote(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    upvote = Upvote.objects.get_or_create(user=user, post=post)
    post.amount_of_upvotes += 1
    post.save()
    return JsonResponse({'success': 'upvote successfully added'}, status=status.HTTP_200_OK)

@transaction.non_atomic_requests
@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_upvote(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    upvote = get_object_or_404(Upvote, user=user, post=post)
    upvote.delete()
    post.amount_of_upvotes -= 1
    post.save()
    return JsonResponse({'success': 'upvote successfully deleted'}, status=status.HTTP_200_OK)
