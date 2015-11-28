from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^\d*/$', 'courses.views.detail', name='detail'),   
)
