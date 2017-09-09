from django.db import models
from django.conf import settings
from stdimage.models import StdImageField

def upload_location(party, filename):
    filebase, extension=filename.split(".")
    return "%s/%s.%s" %(party.id, filename, extension)

def beer_img_upload_location(name, filename):
    filebase, extension=filename.split(".")
    return "%s.%s" %(name, extension)

# Create your models here.
class BeerType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Production_Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # nation                = models.CharField(max_length=30, null=True)
    # location          = models.CharField(max_length=30, null=True)
    # owner_company     = models.CharField(max_length=50, null=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Beer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    nation = models.CharField(max_length=30)
    # location          = models.CharField(max_length=30)
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    calorie = models.SmallIntegerField(default=43)
    description = models.TextField(default='BEER Description HERE')
    beertype = models.ForeignKey(BeerType, on_delete=models.SET_NULL, null=True, related_name='beertype_beers')
    company = models.ForeignKey(Production_Company, on_delete=models.SET_NULL, null=True,
                                related_name='production_beers')
    reviews_count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    overall_score = models.DecimalField(max_digits=10, decimal_places=9, default=0)
    beer_image=StdImageField(upload_to=beer_img_upload_location, blank=True, variations={'avatar':(32,32), 'main':(270,270)})
    #image_recommend=StdImageField(upload_to=beer_img_upload_location(name), variations={'thumbnail': {'width': 270, 'height': 270}})    
    ### comment from ljh that overall_score need to have default value of 3 or 0
    total_sum = models.DecimalField(max_digits=30, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    # def reviews_count_up(self):
    #   self.reviews_count = self.reviews_count + 1
    #   super(Beer, self).save()


class BeerReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    overall_score = models.DecimalField(max_digits=2, decimal_places=1)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name='beer_reviews')
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ### comment from ljh that for better management review needs to have deleted boolean value and when it is deleted.

    def __str__(self):
        return self.comment
