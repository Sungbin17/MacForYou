from django.contrib import admin
from .models import Meetup

# Register your models here.
# class ChoiceInline(admin. TabularInline):
# 	model= Choice
# 	extra=3

# class PartyAdmin(admin.ModelAdmin):
# 	fieldsets=[
# 		(None,		{'fields': ['title'],}),
# 		(None,		{'fields': ['content']}),
# 		(None,		{'fields': ['place']}),
# 		(None,		{'fields': ['date_meeting']}),
# 	]
# 	inlines=[ChoiceInline]

# 	list_display=('title',)

admin.site.register(Meetup)

