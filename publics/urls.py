from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^refresh/$', views.refresh_movie_list, name='refresh_movie_list'),
    url(r'^watch_movie/$', views.watch_movie, name='watch_movie'),
    url(r'^clear_history/$', views.clear_history, name='clear_history'),
]
