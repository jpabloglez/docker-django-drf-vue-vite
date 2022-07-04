from django.shortcuts import render

from .models import User
from .serializers import UserListSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_auth.registration.views import RegisterView
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.

class UserRegisterView(RegisterView):
    queryset = User.objects.all()

class UserAPIView(APIView):

    @staticmethod
    def get(request):
        users = User.objects.all()
        print("USERS: ", users)
        serializer = UserListSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def users(request):
    '''
    List all analyses operations
    '''
    if(request.method == 'GET'):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        logger.log_info(f"JSON RESPONSE: {serializer.data}")
        return JsonResponse(serializer.data, safe=False)