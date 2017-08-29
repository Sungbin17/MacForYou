from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.review_list, name='review_list'),
    url(r'^create/$', views.review_create, name='review_create'),

]
