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

def gad7Test(request):
    return render(request, 'gad7Test.html')

def phq9Test(request):
    return render(request, 'phq9Test.html')

def k10Test(request):
    return render(request, 'k10Test.html')

def submit_k10(request):
    if request.method == 'POST':
        score = 0
        for i in range(1, 11):
            score += int(request.POST.get(f'q{i}', 0))
            
        if score <= 19:
            feedback = "Low distress"
            detailed_feedback = "Your distress level is low. This indicates good mental health. Continue maintaining a balanced lifestyle with regular physical activity, healthy eating, and a supportive social network."
        elif score <= 24:
            feedback = "Mild distress"
            detailed_feedback = "You are experiencing mild distress. Consider incorporating relaxation techniques such as deep breathing, yoga, or meditation. Talking to a friend or family member about your feelings can also be helpful."
        elif score <= 29:
            feedback = "Moderate distress"
            detailed_feedback = "You are experiencing moderate distress. It may be beneficial to seek support from a mental health professional. Techniques like cognitive-behavioral therapy (CBT) can be effective. Additionally, maintaining a regular routine, exercising, and eating a balanced diet are important."
        elif score <= 34:
            feedback = "High distress"
            detailed_feedback = "You are experiencing high distress. Professional help is recommended. A mental health professional can assist with developing a treatment plan which may include therapy and other supportive measures. Self-care practices and reaching out to your support network are also important."
        else:
            feedback = "Very high distress"
            detailed_feedback = "You are experiencing very high distress. It is crucial to seek professional help immediately. Treatment options include therapy, medication, and support groups. Avoiding alcohol and drugs, getting plenty of rest, and engaging in stress-reducing activities like mindfulness or gentle physical exercise are also recommended."
        return render(request, 'k10Test.html', {'score': score, 'feedback': feedback, 'detailed_feedback': detailed_feedback})
    return render(request, 'k10Test.html')

def submit_gad7(request):
    if request.method == 'POST':
        score = 0
        for i in range(1, 8):
            score += int(request.POST.get(f'q{i}', 0))
            
        if score <= 4:
            feedback = "Minimal anxiety"
            detailed_feedback = "Your anxiety level is minimal. This is a positive indicator of your mental health. Continue to maintain a healthy lifestyle, engage in regular physical activity, and practice relaxation techniques like deep breathing or meditation."
        elif score <= 9:
            feedback = "Mild anxiety"
            detailed_feedback = "You are experiencing mild anxiety. Consider incorporating relaxation techniques into your daily routine, such as yoga, meditation, or deep breathing exercises. It may also be helpful to talk to a trusted friend or family member about your feelings."
        elif score <= 14:
            feedback = "Moderate anxiety"
            detailed_feedback = "You are experiencing moderate anxiety. It might be beneficial to seek support from a mental health professional. Cognitive-behavioral therapy (CBT) is effective in treating anxiety. Additionally, consider lifestyle changes such as regular exercise, a balanced diet, and sufficient sleep."
        else:
            feedback = "Severe anxiety"
            detailed_feedback = "You are experiencing severe anxiety. It is important to seek professional help as soon as possible. A mental health professional can work with you to develop a treatment plan, which may include therapy and/or medication. In the meantime, try to avoid caffeine, get plenty of rest, and practice stress-reducing activities like mindfulness or gentle physical exercise."
        return render(request, 'gad7Test.html', {'score': score, 'feedback': feedback, 'detailed_feedback': detailed_feedback})
    
    return render(request, 'gad7Test.html')

def submit_phq9(request):
    if request.method == 'POST':
        score = 0
        for i in range(1, 10):
            score += int(request.POST.get(f'q{i}', 0))
            
        if score <= 4:
            feedback = "Minimal depression"
            detailed_feedback = "Your depression level is minimal. Continue maintaining a healthy lifestyle with regular physical activity and a balanced diet. Ensure you have a support system and engage in activities that you enjoy."
        elif score <= 9:
            feedback = "Mild depression"
            detailed_feedback = "You are experiencing mild depression. Consider incorporating relaxation techniques such as mindfulness or meditation. It's helpful to talk to a trusted friend or family member about your feelings. Monitoring your mood and maintaining a regular routine can also be beneficial."
        elif score <= 14:
            feedback = "Moderate depression"
            detailed_feedback = "You are experiencing moderate depression. It is advisable to seek support from a mental health professional. Cognitive-behavioral therapy (CBT) and other therapeutic approaches can be effective. Lifestyle changes like regular exercise, a balanced diet, and sufficient sleep are also important."
        elif score <= 19:
            feedback = "Moderately severe depression"
            detailed_feedback = "You are experiencing moderately severe depression. Professional help is strongly recommended. A mental health professional can work with you on a treatment plan which may include therapy and possibly medication. In the meantime, practice self-care and reach out to your support network."
        else:
            feedback = "Severe depression"
            detailed_feedback = "You are experiencing severe depression. It is critical to seek professional help immediately. Treatment options include therapy, medication, and support groups. Avoid alcohol and drugs, get plenty of rest, and engage in stress-reducing activities like mindfulness or gentle physical exercise."
        return render(request, 'phq9Test.html', {'score': score, 'feedback': feedback, 'detailed_feedback': detailed_feedback})
        
    return render(request, 'phq9Test.html')

def stressPage(request):
    return render(request, 'stress.html')

def anxietyPage(request):
    return render(request, 'anxiety.html')

def resiliencePage(request):
    return render(request, 'resilience.html')