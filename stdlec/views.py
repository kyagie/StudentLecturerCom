from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, SendEmailForm
from django.core.mail import BadHeaderError, send_mail


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
    
def emailView(request):
    if request.method == 'GET':
        form = SendEmailForm()
    else:
        form = SendEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']
            try:
                send_mail(subject,message,from_email,[recipient])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('landing')
    return render(request, "email.html", {'form': form})

