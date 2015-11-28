from django.shortcuts import get_object_or_404, render
from courses.models import Course, Lesson

#def detail(request):
#    qs_courses = Course.objects.all()
#    return render(request, 'courses/detail.html', {
#          'courses': qs_courses,
#        })
        
def detail(request, course_id):
    print course_id
    courses = get_object_or_404(Course, id=course_id)
    lessons = get_object_or_404(Lesson, course=course_id)
    return render(request, 'courses/detail.html', {
                  'courses': courses,
                  'lessons': lessons,
           })        
