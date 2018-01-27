from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^travels$',views.home),
    url(r'^books/add/$', views.addtrip),
    url(r'^newtrip$', views.newtrip),
    url(r'^users/(?P<id>\d+)$', views.userpage),
    url(r'^join/(?P<id>\d+)$', views.join)
]