from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
	url(r'^profile/',views.profile, name='profile'),
]