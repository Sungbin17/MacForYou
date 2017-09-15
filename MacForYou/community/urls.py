from django.conf.urls import url
from . import views

app_name = 'community'
urlpatterns = [
	url(r'^$', views.meetup_view, name='meetup'),
	url(r'^(?P<meetup_id>[0-9]+)/$', views.meetup_detail, name='meetup_detail'),
	#url(r'^(?P<party_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<party_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^create$', views.party_create, name='create'),
	#url(r'^choice_create$', views.choice_create, name='choice_create'),
	url(r'^(?P<pk>\d+)/likes/$', views.party_likes, name='meetup_likes'), 

]