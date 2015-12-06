from students.models import Student
from django.forms import ModelForm
from courses.models import Course, Lesson


class CourseModelForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class LessonModelForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
