from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("landing", views.loginn, name="loginn"),
    path('', views.index, name="index"),
    path('landing/', views.landing, name="landing"),
    path('email/', views.emailView, name='email')
]
