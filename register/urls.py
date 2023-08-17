from django.urls import path
from . import views
from .forms import registration_view

urlpatterns = [
    # Define your app's URL patterns here
    path('register/', views.register_user, name='register_user'),
    # Add more URL patterns as needed
]
