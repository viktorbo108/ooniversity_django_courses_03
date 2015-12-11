from django.shortcuts import render
from courses.models import Course
from django.contrib import messages


def index(request):
    qs_courses = Course.objects.all()
    return render(request, 'index.html', {
          'courses': qs_courses,
        })

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')
    
class MixinTitle(object):
    def get_context_data(self, **kwargs):
        data = super(MixinTitle, self).get_context_data(**kwargs)
        data['title'] = self.title
        return data

class MixinMsg(object):
    def form_valid(self, form):
        messages.success(self.request, self.success_message['msg'] %
                         form.save().__getattribute__(self.success_message['attr']))
        return super(MixinMsg, self).form_valid(form)

