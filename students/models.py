# -*- coding: utf-8 -*-

from django.db import models
from courses.models import Course
from django.forms import ModelForm

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
    
    def __unicode__(self):
        return self.name
        
