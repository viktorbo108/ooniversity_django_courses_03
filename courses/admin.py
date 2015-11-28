from django.contrib import admin
from courses.models import Lesson, Course

admin.site.register(Course)
admin.site.register(Lesson)

