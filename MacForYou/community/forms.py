from django import forms
from .models import Party, Choice
from django.forms import DateTimeField



class PartyModelForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['title', 'content', 'preferred_beer', 'place', 'date_meeting', ]

class ChoiceModelForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['party', 'choice_text',]





