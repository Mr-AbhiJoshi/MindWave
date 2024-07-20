from django.shortcuts import render, HttpResponse

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