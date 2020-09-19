from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, SendEmailForm
from django.core.mail import send_mail


# Create your views here.
# views.py


# Create your views here.
def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/accounts/login/")
    else:
	    form = RegisterForm()

    return render(response, "registration/register.html", {"form":form})

def loginn(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("landing/")
    else:
        return HttpResponse("User not found")
          # Return an 'invalid login' error message.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def landing(request):
    template = loader.get_template('landing.html')
    return HttpResponse(template.render())

def sendemail(request):
    if response.method == "POST":
        form = SendEmailForm(response.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']    
            recipients = form.cleaned_data['recipient']
            
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
	    form = SendEmailForm()

    return render(response, "landing.html", {"form":form})