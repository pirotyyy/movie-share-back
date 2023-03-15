from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'post_title', 'created_at', 'author', 'movie', 'evaluation', 'impression')