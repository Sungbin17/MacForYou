from django.contrib import admin
from .models import Suggestions

# Register your models here.

@admin.register(Suggestions)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'created_at', 'updated_at' ]



