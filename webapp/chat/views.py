import datetime

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from chat.models import ConnectedUsers


# def index(request):
#     return render(request, 'chat/index.html')

@login_required
def room(request):
    return render(request, 'chatroom.html', {
        'room_name': 'chatroom'
    })


@login_required
def webhook(request):
    channel_layer = get_channel_layer()
    if not channel_layer.groups:
        return HttpResponse('No any groups available')
    async_to_sync(channel_layer.group_send)(
        list(channel_layer.groups.keys())[0],
        {
            'type': 'chat_message',
            'message': 'Hello from the Web. Current time is %s' % datetime.datetime.now()
        }
    )
    return HttpResponse("Result is OK. Check windows of the firstly created chat for a new message")


@staff_member_required
def users_online(request):
    connected_users = [str(user) for user in ConnectedUsers.objects.all()]
    return render(request, 'chat\online.html', {
        'connected_users': connected_users
    })
