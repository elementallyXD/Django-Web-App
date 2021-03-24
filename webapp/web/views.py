from .models import Todo
from .serializers import TodoSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.


class TodoViewSet1(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def dashboard(request):
    return render(request, "about/about.html")
