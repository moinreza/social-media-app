# social_media/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # Include posts app URLs for homepage
    path('users/', include('users.urls')),  # Include users app URLs
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Redirect to homepage after logout
]
