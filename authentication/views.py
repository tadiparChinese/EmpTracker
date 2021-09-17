import math
import datetime
from django.utils import dateparse

from django.contrib import messages
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status, response
from rest_framework.exceptions import ParseError
from rest_framework import permissions

# from django.core.cache import cache

from rest_framework.views import APIView

from authentication.serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView


class AuthUserAPI(GenericAPIView):
    permission_classes =(permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user=user)
        return response.Response({'user':serializer.data})


# Register API
class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Login API
class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message':'Invalid Credentials try again'}, status=status.HTTP_401_UNAUTHORIZED)