import math
import datetime
from django.utils import dateparse

from django.contrib import messages

from django.shortcuts import redirect

from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer

from django.core.exceptions import ValidationError

from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import permissions

# from django.core.cache import cache

from rest_framework.views import APIView

from authentication.serializers import RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 