from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.register),
    url(r'^logout/$', views.logout),
    url(r'^travels$',views.home),
    url(r'^travels/add/$', views.addtrip),
    url(r'^newtrip$', views.newtrip),
    url(r'^travels/destination/(?P<id>\d+)$', views.destination),
    url(r'^join/(?P<id>\d+)$', views.join)
]