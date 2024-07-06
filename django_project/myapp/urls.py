# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line for the root URL
    path('hello/', views.hello_world, name='hello_world'),  # Example additional URL
]