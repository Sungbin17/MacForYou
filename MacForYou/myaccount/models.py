from django.conf import settings
from django.db import models

# Create your models here.

class UserProfile(models.Model):
	#it is not wise to user User model directly from django.contrib.auth.models 
	#it is wise to user this way
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
	nickname = models.CharField(max_length=30, unique=True)
	is_premium = models.BooleanField(default=False)

	def __str__(self):
		return self.nickname
