from django.db import models
from django.conf import settings
from stdimage.models import StdImageField

def beer_img_upload_location(name, filename):
    filebase, extension=filename.split(".")
    return "%s.%s" %(name, extension)

# Create your models here.
class BeerType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    #TODO : img field required
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Production_Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # nation = models.CharField(max_length=30, null=True)
    # location          = models.CharField(max_length=30, null=True)
    # owner_company = models.CharField(max_length=50, null=True)
    description = models.TextField()
    #TODO: image field required
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Beer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    nation = models.CharField(max_length=30)
    # location          = models.CharField(max_length=30)
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    #calorie = models.SmallIntegerField(default=43)
    description = models.TextField(default='BEER Description HERE')
    beertype = models.ForeignKey(BeerType, on_delete=models.SET_NULL, null=True, related_name='beertype_beers')
    company = models.ForeignKey(Production_Company, on_delete=models.SET_NULL, null=True, related_name='production_beers')
    overall_score = models.DecimalField(max_digits=10, decimal_places=9, default=0)
    beer_image=StdImageField(upload_to=beer_img_upload_location, blank=True, variations={'avatar':(32,32), 'main':(270,270)})  
    total_sum = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    reviews_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #TODO: add search field to or korea name field to search on korean keyword and show up on reasult

    def __str__(self):
        return self.name

    # def reviews_count_up(self):
    #   self.reviews_count = self.reviews_count + 1
    #   super(Beer, self).save()


class BeerReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name='beer_reviews')
    overall_score = models.DecimalField(max_digits=3, decimal_places=2)    
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.comment