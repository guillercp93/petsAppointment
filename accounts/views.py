from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from accounts.serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer