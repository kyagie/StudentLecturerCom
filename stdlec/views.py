from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

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


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def landing(request):
    template = loader.get_template('landing.html')
    return HttpResponse(template.render())