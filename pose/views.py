from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def nam(request):
    return render(request,'gamani.html')
# def name(request):
#     return render(request,'link.html')
# # views.py

def home(request):
    return render(request,'gamani.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change 'home' to the URL name of your home page
        else:
            error_message = 'Invalid login credentials'
            return render(request, 'link.html', {'error_message': error_message})
    else:
        return render(request, 'link.html')

# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=name, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            return redirect('success_page')
        else:
            # Authentication failed, handle accordingly (e.g., show an error message)
            return render(request, 'new.html', {'error': 'Invalid credentials'})

    return render(request, 'new.html')

def success_page_view(request):
    return render(request, 'link.html')
# views.py
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

def send_email(request):
    subject = 'Subject of the email'
    message = 'Body of the email'
    from_email = 'gamanin79@example.com'
    recipient_list = ['gamaniprasad6@example.com']

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Email sent successfully!')
# def vose(request):
#     return render(request,'ok.html')
from django.http import HttpResponse

def page(request):
    return HttpResponse("Good going good")
from django.shortcuts import render, redirect

def vose(request):
    if request.method == 'POST':
        # Process the form submission here
        # Redirect to 'good' URL upon successful submission
        return redirect('good')
    return render(request, 'ok.html')
from .models import job

def fine(request):
    data = job.objects.all()  # Retrieve all objects from the Job model
    return render(request, 'good.html', {'data': data})







