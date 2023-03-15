from django.shortcuts import render

from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from .models import User

from .serializers import UserSerializer

# Create your views here.
class UserRegister(generics.CreateAPIView):
  permission_classes = [AllowAny] 
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def post(self, request, format=None):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    raise ParseError(detail='このEメールまたはユーザー名はすでに使われています。') 