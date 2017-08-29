from django.contrib import admin
from .models import Beer, BeerType, Production_Company, BeerReview
# Register your models here.
admin.site.register(Beer)
admin.site.register(BeerType)
admin.site.register(Production_Company)
admin.site.register(BeerReview)