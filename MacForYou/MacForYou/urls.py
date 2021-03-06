"""MacForYou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings


from beereview.views import  beer_type, index_view, user_review_list

# def root(request):
#     return render(request, 'root.html')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^beer/full_list/$', BeerListView.as_view()),
    # url(r'^beer/(?P<slug>[\w-]+)/$', BeerDetailView.as_view()),
    url(r'^beertype/(?P<slug>[\w-]+)/$', beer_type, name='beer_type'),
    url(r'^user/(?P<pk>\d+)/$', user_review_list, name='user_review_list'),
    url(r'^beers/', include('beereview.urls', namespace='beers')),
    url(r'^community/', include('community.urls', namespace='community')),
    url(r'^$', index_view, name='index'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
