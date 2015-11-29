from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, ch):
    coaches = Coach.objects.get(id=ch)

    courses = Course.objects.filter(coach=ch)
    assistants = Course.objects.filter(assistant=ch)
    return render(request, 'coaches/detail.html', {
        'coaches': coaches,
        'courses': courses,
        'assistants': assistants})