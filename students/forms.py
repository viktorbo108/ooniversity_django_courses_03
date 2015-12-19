# -*- coding: utf-8 -*-

from students.models import Student
from django import forms

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
