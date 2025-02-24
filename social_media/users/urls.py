# users/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

# from django.urls import path
# from django.contrib.auth.views import LoginView
# from . import views

# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('logout/', views.user_logout, name='logout'),
# ]
