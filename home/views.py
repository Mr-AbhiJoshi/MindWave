from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/')
    
    return render(request, 'index.html')
    #return HttpResponse('This is homepage')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request,"Your message has been sent")
    return render(request, 'contact.html')

def coverpage(request):
    return render(request, 'coverpage.html')

def signupUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request,"Sign Up Successful")
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')
    return render(request, 'coverpage.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
    
        if user is not None:
            login(request, user)
            messages.success(request,"Login Successful")
            return redirect("/index")
        else:
            messages.error(request, 'Login Unsuccessful')
            return redirect("/")

def logoutUser(request):
    logout(request)
    return redirect('/')

def avatar(request):
    return render(request, 'avatar.html')

def vWorld(request):
    return render(request, 'vworld.html')

def community(request):
    return render(request, 'community.html')

def therapist(request):
    return render(request, 'therapist.html')

def assessment(request):
    return render(request, 'assessment.html')

def resources(request):
    return render(request, 'resources.html')

def game1(request):
    return render(request, 'game1.html')

def game2(request):
    return render(request, 'game2.html')