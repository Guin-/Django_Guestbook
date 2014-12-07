from django.conf.urls import patterns, url

from gbook import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)




