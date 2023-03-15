from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import UserRegister

urlpatterns = [
  path('register/', UserRegister.as_view())
]