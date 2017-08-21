from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse

# Create your views here.
from .models import Beer, BeerType, Production_Company

#ClassBaseView
class BeerDetailView(DetailView):
	template_name = 'beer_detail.html'

	def get_object(self, *args, **kwargs):
		name = self.kwargs.get("slug")
		instance = get_object_or_404(Beer, name__iexact=name) #iexact make nonecase sensetive db search
		return instance

	def get_context_data(self, *args, **kwargs):
		context = super(BeerDetailView, self).get_context_data(*args, **kwargs)
		return context

class BeerTypeDetailView(DetailView):
	template_name = 'beertype_detail.html'

	def get_object(self, *args, **kwargs):
		name = self.kwargs.get("slug")
		instance = get_object_or_404(BeerType, name__iexact=name) #iexact make nonecase sensetive db search
		return instance

	def get_context_data(self, *args, **kwargs):
		context = super(BeerTypeDetailView, self).get_context_data(*args, **kwargs)
		context['beertype_beers_list'] = context['object'].beertype_beers.all()
		
		return context

# class BeerTypeDetailView(View):
	
# 	def get(self, request, *args, **kwargs):
# 		name = 'lager'
# 		instance = get_object_or_404(BeerType, name__iexact=name)
# 		print(instance.beertype_beers.all())
# 		return HttpResponse('debuging')
