from django.contrib import admin 
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('post.urls')),
    path('api/users/', include('user.urls')),
    path('api/auth/', include('auth.urls')) 
]