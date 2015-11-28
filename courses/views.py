from django.shortcuts import render
from courses.models import Course

def detail(request):
    qs_courses = Course.objects.all()
    return render(request, 'courses/detail.html', {
          'test': "Privet",
        })
