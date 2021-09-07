from django.shortcuts import render

# Create your views here.
def homepageview(request):
    return render(request, 'index.html')

def roomview(request):
    room_no=request.POST['room_no'],
    name=request.POST['name'],
    return render(request, 'room.html', {'room_no':room_no, 'name': name})

