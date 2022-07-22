import imp
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import userEvent
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.storage import FileSystemStorage

def index(request):
    event_obj = userEvent.objects.all()
    params = {'events' : event_obj}
    return render(request, 'index.html', params)

def home(request):
    event_id = request.GET.get('id')
    event_obj = userEvent.objects.filter(event_id = event_id).first()
    user = event_obj.reguser
    user_obj = User.objects.filter(username = user).first()
    user_n = user_obj.first_name[0:10]
    params = { 'event' : event_obj, 'user' : user_obj, 'user_n' : user_n}
    return render(request, 'home.html', params)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('/profile')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if User.objects.filter(email = email).exists():
            messages.warning(request, "Email already exists")
            return redirect('/signup')

        if User.objects.filter(username = username).exists():
            messages.warning(request, "Username already exists")
            return redirect('/signup')
        
        if(password != cpassword):
            messages.warning(request, "Passwords dosen't match")
            return redirect('/signup')

        user = User(username=username, email=email, first_name=name)
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('/login')
    return render(request, 'signup.html')
    
def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('/login')

@login_required(login_url = '/login/')
def createEventView(request):
    if request.method == "POST":
        image = request.FILES.get('file')
        heading = request.POST.get('head')
        day = request.POST.get('day')
        month = request.POST.get('month')
        start_time = request.POST.get('stime')
        end_time = request.POST.get('etime')
        location = request.POST.get('loc')
        user = request.user
        user_obj = User.objects.filter(username = user).first()
        print(user_obj)
        im = Image.open(image)
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        filepath = fs.url(filename)
        event = userEvent(reguser = user_obj, image = filepath, heading = heading, day = day, month = month, start_time = start_time, end_time = end_time, location = location)
        event.save()
        messages.success(request, "Event added successfully")
    return render(request, 'create-event.html')

@login_required
def profile(request):
    user = request.user
    user_obj = User.objects.filter(username = user).first()
    event_obj = userEvent.objects.filter(reguser = user).all()
    params = { 'user' : user_obj, 'event' : event_obj}
    return render(request, 'profile.html', params)