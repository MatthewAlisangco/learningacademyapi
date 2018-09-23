from django.shortcuts import render
from rest_framework import viewsets
from .models import Users
from .userserializers import UsersSerializer
# Create your views here.
# Updates UserTable

class UsersView (viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer