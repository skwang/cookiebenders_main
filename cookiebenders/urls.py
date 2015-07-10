from django.conf.urls import patterns, url
from cookiebenders import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^get_cost/', views.get_cost, name='get_cost')
        )