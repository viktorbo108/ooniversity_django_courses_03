from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', 'courses.views.detail', name='detail'),   
    url(r'^edit/(?P<course_id>\d+)/$', 'courses.views.edit', name='edit'),   
    url(r'^remove/(?P<course_id>\d+)/$', 'courses.views.remove', name='remove'),   
    url(r'^add/$', 'courses.views.add', name='add'),   
    url(r'^(?P<course_id>\d+)/add_lesson/$', 'courses.views.add_lesson', name='add_lesson'),   
)
