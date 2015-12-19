# -*- coding: utf-8 -*-

from courses.models import Course, Lesson
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import logging

logger = logging.getLogger(__name__) # __name__ = courses.views


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        pk = self.object.pk
        courses = Course.objects.get(id=pk)
        logger.debug('Courses detail view has been debugged') 
        logger.info('Logger of courses detail view informs you!') 
        logger.warning('Logger of courses detail view warns you!') 
        logger.error('Courses detail view went wrong!') 
        lessons = courses.lesson_set.all()
        coaches = courses.coach.user.get_full_name()
        assistants = courses.assistant.user.get_full_name()
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['course_id' ] = pk
        context['courses' ] = courses
        context['lessons' ] = lessons
        context['coach' ] = coaches
        context['assistent' ] = assistants
        return context

        
class CourseCreateView(CreateView):
    model = Course
    template_name = "courses/add.html"
    success_url = '/'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title' ] = "Course creation"
        return context
    
    def form_valid(self, form):
        course_name = self.request.POST
        messages.add_message(self.request, messages.INFO, 
                             'Course %s has been successfully added.' % course_name['name'] )
        return super(CourseCreateView, self).form_valid(form)
        
        
class CourseUpdateView(UpdateView):
    model = Course
    template_name = "courses/edit.html"
    context_object_name = 'course'
   
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title' ] = "Course update"
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)
        
    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('courses:edit', kwargs={'pk': pk})
        
        
class CourseDeleteView(DeleteView):
    model = Course
    template_name = "courses/remove.html"
    success_url = reverse_lazy('index')
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        ret_message = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Course %s has been deleted.' % (self.object.name))
        return ret_message
    

class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title' ] = 'Lesson creation'
        return context
    
    def form_valid(self, form):
        form.save()
        course_name = self.request.POST
        messages.add_message(self.request, messages.INFO, 
                             'Lesson %s has been successfully added.' % course_name['subject'] )
        return super(LessonCreateView, self).form_valid(form)
        
    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('courses:add_lesson', kwargs={'pk': pk})
        
    def get_initial(self):
        return {'course': self.kwargs['pk']}
        
