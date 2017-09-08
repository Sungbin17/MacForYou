from django.contrib import admin
from .models import Party, Choice
# Register your models here.
class ChoiceInline(admin. TabularInline):
	model= Choice
	extra=3

class PartyAdmin(admin.ModelAdmin):
	fieldsets=[
		(None,		{'fields': ['title'],}),
		(None,		{'fields': ['content']}),
		(None,		{'fields': ['preferred_beer']}),
		(None,		{'fields': ['place']}),
		(None,		{'fields': ['date_meeting']}),
		(None,		{'fields': ['party_beer_image']}),
		(None,		{'fields': ['height_field']}),
		(None,		{'fields': ['width_field']}),
	]
	inlines=[ChoiceInline]

	list_display=('title',)

admin.site.register(Party, PartyAdmin)

