import json
from rest_framework import status
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from .serializers import *
from .models import Comments
from blog_engine.models import Post
# Create your views here.

@api_view(["GET"])
@csrf_exempt
@permission_classes([AllowAny])
def show_post_comments(request, post_id):
    comments = Comments.objects.filter(related_post__id=post_id)
    serializer = CommentSerializerRead(comments, many=True)
    return JsonResponse({'posts': serializer.data}, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_comment(request, post_id):
    data = json.loads(request.body)
    author_name = request.user
    new_comment = Comments.objects.create(content=data['content'],
                                          author_name=author_name,
                                          related_post=Post.objects.get(id=post_id))
    serializer = CommentSerializerRead(new_comment)
    return JsonResponse({'new_post': serializer.data}, status=status.HTTP_200_OK)

@transaction.non_atomic_requests
@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comments, author_name=request.user, id=comment_id)
    comment.delete()
    return JsonResponse({f'Post {comment.id}': 'successfully deleted'}, status=status.HTTP_200_OK)

@transaction.non_atomic_requests
@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_comment(request, comment_id):
    comment = get_object_or_404(Comments, author_name=request.user, id=comment_id)
    data = json.loads(request.body)
    comment.content = data['content']
    comment.save()
    serializer = CommentSerializerUpdate(comment)
    return JsonResponse({'new_post': serializer.data}, status=status.HTTP_200_OK)
