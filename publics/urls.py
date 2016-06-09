from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^refresh/$', views.refresh_movie_list, name='refresh_movie_list'),
]
