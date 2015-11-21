from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    #return HttpResponse("Ok!")
    return render(request, 'index.html')

def contact(request):
    #return HttpResponse("Ok!")
    return render(request, 'contact.html')

def student_list(request):
    #return HttpResponse("Ok!")
    return render(request, 'student_list.html')

def student_detail(request):
    #return HttpResponse("Ok!")
    return render(request, 'student_detail.html')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main, name='home'),
    url(r'^contact.html/$', contact, name='contact'),
    url(r'^student_detail.html/$', student_detail, name='student_detail'),

    url(r'^admin/', include(admin.site.urls)),
)
