from django.shortcuts import get_object_or_404, render
from courses.models import Course, Lesson


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