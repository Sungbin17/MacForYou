from django import forms
from .models import Party, Choice


class PartyModelForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['title', 'content', 'preferred_beer', 'place', 'date_meeting', 'pub_date']