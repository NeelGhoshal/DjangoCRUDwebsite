from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms} #Context based as a python dictionary
    return render(request, 'base/home.html', context)

def rooms(request, pk):
    room = Room.objects.get(id=pk)  #getting rooms from database via id, pk = primary key
    context = {'room' : room}
    
    return render(request, 'base/rooms.html',context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST) #adding POST data to the form type we have made
        if form.is_valid(): #if valid type
            form.save() #Data posted will be saved in the format of form
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) #initial gets the values of an item from the database which is passed here
    
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room) #this will overwrite the data in the given specific instance
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})