from .models import Todo
from django.shortcuts import render, redirect
from .serializers import TodoSerializer, UserSerializer, CreateUserForm
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
# Create your views here.


class TodoViewSet1(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = (TokenAuthentication,)


class UserViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'webapp/accounts/templates/registration/signup.html', context)


def dashboard(request):
    return render(request, "about/about.html")
