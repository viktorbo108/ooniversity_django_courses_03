# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages


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
    
def add(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            surname = data['surname']
            name = data['name']
            student_added = 'Студент успешно добавлен'
            new_student = StudentModelForm(request.POST)
            res = new_student.save()
            # messages for success form data:
            messages.success(request, student_added)
            return redirect('students:list_view')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student_edited = 'Данные изменены'
            edited_student = StudentModelForm(request.POST, instance=student)
            res = edited_student.save()
            # messages for success form data:
            messages.success(request, student_edited)
            return redirect('/students/edit/'+student_id)
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})

def delle(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        student_edited = 'Данные удалены'
        # messages for success form data:
        messages.success(request, student_edited)
        return redirect('students:list_view')
    return render(request, 'students/delle.html')



    