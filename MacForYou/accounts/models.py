from django.db import models
from django.contrib.auth.models import User

class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'cp_user')
    name = models.CharField(max_length=254, null=True, blank=True,)
    score = models.IntegerField()
    number_of_posts = models.IntegerField()

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return self.name
