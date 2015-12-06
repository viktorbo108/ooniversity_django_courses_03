# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, course_id):
    courses = Course.objects.get(id=course_id)
    lessons = courses.lesson_set.all()
    coaches = courses.coach.user.get_full_name()
    assistants = courses.assistant.user.get_full_name()
    return render(request, 'courses/detail.html', {
                      'courses': courses,
                      'course_id': course_id,
                      'lessons': lessons,
                      'coach': coaches,
                      'assistent': assistants,
                  })           
				  
def add(request):
    if request.method == 'POST':
      form = CourseModelForm(request.POST)
      if form.is_valid():
          data = form.cleaned_data
          course_name  = data['name']
          add_message = 'Course %s has been successfully added.' % course_name
          new_course = CourseModelForm(request.POST)
          result = new_course.save()
          messages.success(request, add_message)
          return redirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
      form = CourseModelForm(request.POST, instance=course)
      if form.is_valid():
          add_message = 'The changes have been saved.'
          edited_course = CourseModelForm(request.POST, instance=course)
          result = edited_course.save()
          messages.success(request, add_message)
          return redirect('/courses/edit/%i' % course.id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course_name = course.name
        course.delete()
        rm_message = "Course %s has been deleted." % course_name
        messages.success(request, rm_message)
        return redirect('index')
    return render(request, 'courses/remove.html')
    
def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            course_subject  = data['subject']
            add_message = 'Course %s has been successfully added.' % course_subject
            new_lesson = LessonModelForm(request.POST)
            result = new_lesson.save()
            messages.success(request, add_message)
            return redirect('/courses/%i' % int(course_id))

    else:
        form = LessonModelForm(initial={'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})
