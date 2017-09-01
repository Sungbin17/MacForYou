from django.conf.urls import url
from . import views

app_name = 'community'
urlpatterns = [
	url(r'^$', views.party_view, name='party'),
	url(r'^(?P<party_id>[0-9]+)/$', views.party_detail, name='party_detail'),
	url(r'^(?P<party_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<party_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^create$', views.party_create, name='create'),
	url(r'^choice_create$', views.choice_create, name='choice_create'),
]