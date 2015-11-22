from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
    #url(r'^results/(?P<a>\d+)/(?P<b>\d+)/(?P<c>\d+)$', views.quadratic_results, name='results'),
    url(r'^results/$', views.quadratic_results, name='results'),
)
