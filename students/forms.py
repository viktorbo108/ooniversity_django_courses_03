from students.models import Student
from django.forms import ModelForm

class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
