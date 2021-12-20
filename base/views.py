from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'General Ruwe Room'},
    {'id':2, 'name':'Ruwe Diocese Room'},
    {'id':3, 'name':'Kisii-Nairobi Diocese Room'},
    {'id':4, 'name':'Mombasa Diocese Room'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None

    for i in rooms:
        if i['id'] == int(pk):
            room = i

    context = {'room':room}
    return render(request, 'base/room.html', context)
