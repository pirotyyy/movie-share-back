from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostListView, PostDetailView, PostUpdateView, PostCreateView

urlpatterns = [
  path('list/', PostListView.as_view()),
  path('create/', PostCreateView.as_view()),
  path('detail/<str:pk>', PostDetailView.as_view()),
  path('detail/<str:pk>/edit', PostUpdateView.as_view())
]
