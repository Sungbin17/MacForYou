from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.review_list, name='review_list'),
    url(r'^create/$', views.review_create, name='review_create'),
    url(r'^(?P<pk>\d+)/detail', views.beer_detail, name='beer_detail'),
url(r'^(?P<pk>\d+)/type', views.beer_type, name='beer_type'),
    url(r'^(?P<pk>\d+)/edit', views.review_edit, name='review_edit'),
    url(r'^(?P<pk>\d+)/del', views.review_delete,name='review_delete'),
    url(r'^(?P<pk>\d+)/', views.review_detail, name='review_detail'),


]
