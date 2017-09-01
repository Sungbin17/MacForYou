from django.db import models
import datetime
from django.db import models
from django.utils import timezone


class Party(models.Model):
	title= models.CharField(max_length=200)
	content= models.TextField()
	preferred_beer= models.CharField(max_length=200)
	place= models.CharField(max_length=200)
	date_meeting= models.DateTimeField('date meeting')
	pub_date= models.DateTimeField('date published')

	def __str__(self):
		return self.title
		
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	party = models.ForeignKey(Party, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text