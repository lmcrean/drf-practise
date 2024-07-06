#django_project/myapp/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the homepage!")

def hello_world(request):
    return HttpResponse("Hello, world!")

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)