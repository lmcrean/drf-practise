#django_project/core/urls.py

from django.contrib import admin
from django.urls import path, include
from myapp.views import HelloWorld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the URLs from `myapp`
    path('api/', HelloWorld.as_view(), name='hello_world'),
]