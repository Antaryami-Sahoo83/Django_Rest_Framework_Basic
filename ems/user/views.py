from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from user.serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


# http://127.0.0.1:8000/auth/user/user/ (For testing in the postman)