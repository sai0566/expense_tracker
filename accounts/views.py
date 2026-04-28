from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView
from accounts.models import User
from accounts.serializers import RegisterSerializers

class RegisterView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializers
