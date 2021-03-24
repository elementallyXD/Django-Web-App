from .models import Todo, Category
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer, CategorySerializer
from django.contrib.auth.mixins import LoginRequiredMixin

# Todo ViewSet
class TodoViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer


# Category ViewSet
class CategoryViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer
