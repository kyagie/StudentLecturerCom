from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("landing", views.loginn, name="loginn"),
    path('', views.index, name="index"),
    path('landing/', views.landing, name="landing"),
    path('email/', views.emailView, name='email'),
    path('students/', views.student),
    path('show/', views.show),
    path('edit/<int:id>',views.edit ),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete)
]
