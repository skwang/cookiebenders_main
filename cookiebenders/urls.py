from django.conf.urls import patterns, url
from cookiebenders import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))