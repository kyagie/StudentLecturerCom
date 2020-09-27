from django.db import models

# Create your models here.
class Student(models.Model):
    sfname = models.CharField(max_length=50, blank=False)
    slname = models.CharField(max_length=50, blank=False)
    semail = models.EmailField(blank=False, unique=True)
    sregno = models.CharField(max_length=50, blank=False, unique=True)
    scourse = models.CharField(max_length=50, blank=False)
    scontact = models.IntegerField(blank=False)
    class Meta:
        db_table='student'