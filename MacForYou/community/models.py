from django.db import models
import datetime
from django.db import models
from django.utils import timezone


class Party(models.Model):
	preferred_beer= models.CharField(max_length=200)
	age= models.CharField(max_length=200)
	place= models.CharField(max_length=200)
	date_meeting= models.DateTimeField('date meeting')
	pub_date= models.DateTimeField('date published')

	def __str__(self):
		return self.preferred_beer