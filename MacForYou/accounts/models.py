from django.db import models
from django.contrib.auth.models import User

class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'cp_user')
    name = models.CharField(max_length=254, null=True, blank=True)
    image= models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])

