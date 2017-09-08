from django.conf.urls import url, include

from . import views

urlpatterns = [


    url(r'^$', views.beers_list, name='beers_list'),

    url(r'^type/(?P<slug>[\w-]+)/', views.beer_type, name='beer_type'),

    url(r'^search/(?P<slug>[\w-]+)', views.beer_search, name='beer_search'),

    url(r'^(?P<pk>\d+)/edit', views.review_edit, name='review_edit'),
    url(r'^(?P<pk>\d+)/del', views.review_delete,name='review_delete'),
    url(r'^(?P<slug>[\w-]+)/', views.beer_detail, name='beer_detail'),

    url(r'^(?P<slug>[\w-]+)/create', views.review_create, name='review_create'),




#     url(r'^(?P<pk>\d+)/', views.review_detail, name='review_detail'),


    # url(r'^$', views.full_list, name='full_list'),
    # url(r'^(?P<slug>[\w-]+)/$', views.beer_detail, name='beer_detail'),
 	#url(r'^create/$', views.review_create, name='review_create'),
 	#url(r'^(?P<slug>[\w-]+)/detail', views.beer_detail, name='beer_detail'),
	# url(r'^(?P<slug>[\w-]+)/type', views.beer_type, name='beer_type'),
    # url(r'^(?P<pk>\d+)/edit', views.review_edit, name='review_edit'),
    # url(r'^(?P<pk>\d+)/del', views.review_delete,name='review_delete'),
    # url(r'^(?P<pk>\d+)/', views.review_detail, name='review_detail'),

]
