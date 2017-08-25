from django.db import models
from django.urls import reverse

class Suggestions(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email=models.EmailField()



def get_absolute_url(self):
    return reverse('post:post_list', args=[self.id])