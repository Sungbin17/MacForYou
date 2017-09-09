from django import forms
from .models import Party, Choice
from django.forms import DateTimeField
from datetimewidget.widgets import DateTimeWidget


class PartyModelForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['title', 'content', 'preferred_beer', 'place', 'party_beer_image', 'date_meeting' ]
       	widgets = {
            'date_meeting': forms.DateTimeInput(),
        }

class ChoiceModelForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['party', 'choice_text',]




