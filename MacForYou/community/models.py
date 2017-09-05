from django.db import models
import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.forms import DateTimeField

class Party(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    preferred_beer= models.CharField(max_length=200)
    place= models.CharField(max_length=200)
    date_meeting= models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    likes_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                            blank=True,
                                            related_name='likes_user_set',
                                            through='Likes')


    def __str__(self):
        return self.title
        


class Choice(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Likes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    party = models.ForeignKey(Party)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)