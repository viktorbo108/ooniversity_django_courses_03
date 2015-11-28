from django.shortcuts import render
from students.models import Student


def list_view(request):
    reguest_course = request.GET
    if 'course_id' in reguest_course:
        list_students = Student.objects.filter(
            courses=reguest_course['course_id'])
    else:
        list_students = Student.objects.all()
    return render(request, 'students/list.html', {'list_students': list_students})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})