from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'signin', views.index),
    url(r'login', views.index),
    url(r'logout', views.startpage),
    url(r'^books$',views.home),
    url(r'books/(?P<id>\d+)$', views.singlebook)
]