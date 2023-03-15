from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView

urlpatterns = [
  path('login/', MyTokenObtainPairView.as_view()),
  path('refresh/', TokenRefreshView.as_view())
]