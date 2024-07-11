# myapp/urls.py
from django.urls import path
from . import views
from .views.views_postlist import PostList
from .views.views_welcome import index, hello_world

urlpatterns = [
    path('', views.index, name='index'),  # Add this line for the root URL
    path('hello/', views.hello_world, name='hello_world'),  # Example additional URL
    path('api/posts/', PostList.as_view(), name='post-list'),
]