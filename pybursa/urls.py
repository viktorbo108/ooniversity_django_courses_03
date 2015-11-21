from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views

from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^polls/', include('polls.urls', namespace="polls")),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', pybursa.views.contact, name='contact'),
    url(r'^student_detail/$', pybursa.views.student_detail, name='student_detail'),

    url(r'^admin/', include(admin.site.urls)),
)
