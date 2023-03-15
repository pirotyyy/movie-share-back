from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django_filters import rest_framework as filters

from .models import Post
from .serializers import PostSerializer
from post.utils.permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthorOrReadOnly]
  serializer_class = PostSerializer
  queryset = Post.objects.all()

  def retrieve(self, request):
    filterset = FilterPosts(request.query_params, queryset)
    return Response(seriali)

class FilterPost(filters.FilterSet):
  class Meta:
    model = Post
    fields = '__all__'

class PostListView(generics.ListAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Post.objects.all()

  def get(self, request):
    filterset = FilterPost(request.query_params, queryset=Post.objects.all())
    serializer = PostSerializer(instance=filterset.qs, many=True)
    return Response(serializer.data)

class PostDetailView(generics.RetrieveAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostCreateView(generics.CreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class PostUpdateView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthorOrReadOnly]
  serializer_class = PostSerializer
  queryset = Post.objects.all()
