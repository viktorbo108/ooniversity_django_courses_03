# -*- coding: utf-8 -*-

from students.models import Student
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import logging

logger = logging.getLogger(__name__) # __name__ = students.views
logger_detail = logging.getLogger('students.views.detail') 


class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    paginate_by = 2
    
    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id:
            list_students = Student.objects.filter(courses=course_id)
        else:
            list_students = Student.objects.all()
        return list_students

    def get_context_data(self, **kwargs):
        course_id = self.request.GET.get('course_id')
        context = super(StudentListView, self).get_context_data(**kwargs)
        context['course_id'] = course_id
        return context
        
        
class StudentDetailView(DetailView):
    model = Student
    
    def get_context_data(self, **kwargs):
        #import pdb; pdb.set_trace()
        logger_detail.debug("Students detail view has been debugged")
        logger_detail.info("Logger of students detail view informs you!")
        logger_detail.warning("Logger of students detail view warns you!")
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['title'] = "Student detail"
        return context
    
    
    
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
        
        