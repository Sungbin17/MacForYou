from django.db import models
from django.conf import settings

# def upload_location(party, filename):
#     filebase, extension=filename.split(".")
#     return "%s/%s.%s" %(party.id, filename, extension)

# class Now(models.Model):
#     timenow=datetime.datetime.now()

class Meetup(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title= models.CharField(max_length=30)
    content= models.TextField()
    # preferred_beer= models.CharField(max_length=200)
    # party_beer_image= StdImageField(upload_to=upload_location,
    #  variations={'thumbnail': {'width': 100, 'height': 75}})
    # height_field= models.IntegerField(default=0)
    # width_field= models.IntegerField(default=0)
    place= models.CharField(max_length=200)
    kakao_open_chat_link = models.CharField(max_length=200, blank=True)
    date_meetup= models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# class Choice(models.Model):
#     party = models.ForeignKey(Party, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text

class Mlike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    party = models.ForeignKey(Meetup, on_delete=models.CASCADE, related_name='meetup_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)