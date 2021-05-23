# chat/urls.py
from django.urls import path
from chat.models import ConnectedUsers
from . import views

urlpatterns = [
    path('webhook/', views.webhook),
    path('online/', views.users_online),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]

# from chat.models import ConnectedUsers
ConnectedUsers.objects.all().delete()
