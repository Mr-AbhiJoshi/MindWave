from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable":"My first variable"
    }
    return render(request, 'index.html', context)
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