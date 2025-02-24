# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage that shows posts
    path('profile/', views.profile, name='profile'),  # User profile page
    path('create/', views.create_post, name='create_post'),  # Create post page
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),  # Edit post page
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),  # Delete post page
]
