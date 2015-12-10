# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class StudentListView(ListView):
    model = Student
    context_object_name = 'list_students'
    
    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            list_students = Student.objects.filter(courses=course_id)
        else:
            list_students = Student.objects.all()
        return list_students

        
class StudentDetailView(DetailView):
    model = Student

    
class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, 'Студент добавлен')
        return super(StudentCreateView, self).form_valid(form)

        
class StudentUpdateView(UpdateView):
    model = Student
    
    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('students:edit', kwargs={'pk': pk})
        
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, 'Данные изменены')
        return super(StudentUpdateView, self).form_valid(form)

        
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, 'Данные удалены')
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)
        
        