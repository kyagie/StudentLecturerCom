from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from stdlec.models import Student


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
	    model = User
	    fields = ["username", "first_name", "last_name" ,"email", "password1", "password2"]


class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(required=True)
    recipient_list = forms.EmailField()
    attachment = forms.FileField()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["sfname", "slname", "semail", "sregno", "scourse", "scontact"]
    

   