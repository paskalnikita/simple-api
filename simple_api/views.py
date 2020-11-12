import time
import urllib

# from .models import *
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Message, ViewsCounter
from .functions import client_ip, count_views


def index(request):
    ip = client_ip(request)
    messages = Message.objects.all()
    context = {}
    context['messages'] = []
    for message in messages:
        message_counter = count_views(message, ip)
        context['messages'].append({'message': message, 'counter': message_counter})

    return render(request, 'pages/index.html', context)


def add(request):
    if not request.user.is_authenticated:
        return redirect('/')

    context = {}
    if request.method == 'POST':
        message = str(request.POST.get('message', ''))
        if len(message) > 160:
            context['error'] = 'Message can\'t contain more than 160 char'
            return render(request, 'pages/add.html', context)

        new_message = Message.objects.create(
            user=request.user, message=message, created=datetime.now(tz=timezone.utc))
        ViewsCounter.objects.create(message=new_message, ip=client_ip(request))
        context['success'] = 'Post added!'

    return render(request, 'pages/add.html', context)


def delete(request):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        message_id = str(request.POST.get('id', ''))
        Message.objects.get(user=request.user, id=message_id).delete()

    return redirect('/')


def edit(request, pk=0):
    if not request.user.is_authenticated:
        return redirect('/')

    context = {}
    if request.method == 'GET':
        context['message'] = Message.objects.get(id=pk, user=request.user)

        return render(request, 'pages/edit.html', context)

    if request.method == 'POST':
        edited_message = str(request.POST.get('message', ''))
        mes = Message.objects.get(id=pk, user=request.user)
        mes.message = edited_message
        mes.save()

    return redirect('/')


def me(request):
    return render(request, 'pages/me.html')
