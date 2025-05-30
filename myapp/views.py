from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout
from .models import Room, Topic
from .forms import RoomForm
# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except: 
            messages.error(request, "User does not exist") 

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR password does not exist")
    
    # This needs to be at the same indentation level as the if statement above
    context = {}
    return render(request, 'myapp/login_register.html', context)

def user_logout(request):
    auth_logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all() 
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'myapp/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'myapp/room.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm()
    context = {'form': form}
    return render(request, 'myapp/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')
      

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
          
    context = {'form': form}
    return render(request, 'myapp/room_form.html', context) 

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')
    if request.method == 'POST':
        room.delete()
        return redirect('home')   
    return render(request, 'myapp/delete.html', {'obj': room})