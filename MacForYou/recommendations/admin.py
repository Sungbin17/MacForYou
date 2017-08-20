from django.contrib import admin
from .models import Recommendations

# Register your models here.

@admin.register(Recommendations)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'created_at', 'updated_at' ]



