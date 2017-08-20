from django.conf.urls import url
from .views import BeerDetailView, BeerTypeDetailView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', BeerDetailView.as_view(), name='detail'),
    url(r'^beertype/(?P<slug>[\w-]+)/$', BeerTypeDetailView.as_view(), name='beerdetail'),
]
