from django.db import models

# Create your models here.
class BeerType(models.Model):
	name				= models.CharField(max_length=50, unique=True)
	description			= models.TextField()
	#related_beers		= models.???? OneToMany is needed
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Production_Company(models.Model):
	name				= models.CharField(max_length=50, unique=True)
	description			= models.TextField()
	#related_beers		= models.???? OneToMany is needed
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Beer(models.Model):
	name 				= models.CharField(max_length=50, unique=True)
	nation				= models.CharField(max_length=50)
	abv					= models.DecimalField(max_digits=5, decimal_places=3)
	calorie				= models.SmallIntegerField(default=43)
	description			= models.TextField(default='BEER Description HERE')
	beertype			= models.ForeignKey(BeerType, on_delete=models.SET_NULL, null=True)
	company				= models.ForeignKey(Production_Company, on_delete=models.SET_NULL, null=True)
	#reviews				= models.ManyToManyField()
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name