from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from rest_framework import status

@api_view(["POST"])
@csrf_exempt
@permission_classes([AllowAny])
def login (request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        return JsonResponse({"token": user.auth_token.key})
    else:
        return JsonResponse({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
