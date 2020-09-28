from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your models here.
class Student(models.Model):
    sfname = models.CharField(max_length=50, blank=False)
    slname = models.CharField(max_length=50, blank=False)
    semail = models.EmailField(blank=False, unique=True, validators=[validate_email])
    sregno = models.CharField(max_length=50, blank=False, unique=True)
    scourse = models.CharField(max_length=50, blank=False)
    scontact = models.IntegerField(blank=False)
    class Meta:
        db_table='student'