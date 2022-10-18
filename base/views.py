from django.shortcuts import render
from .models import Room

#rooms = [
#    {'id':1, 'name':'Lets learn python'},
#    {'id':2, 'name':'Design with me'},
#    {'id':3, 'name':'Frontend developers'}
#]

def home(req):
    rooms = Room.objects.all
    context = {'rooms': rooms}
    return render(req, 'base/home.html', context)

def room(req, pk):
    room = Room.objects.get(id=int(pk))
    context = {'room': room}
    return render(req, 'base/room.html', context)

