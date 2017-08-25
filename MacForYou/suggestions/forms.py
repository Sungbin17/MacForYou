from django import forms
from .models import Suggestions


class SuggestionModelForm(forms.ModelForm):
    class Meta:
        model = Suggestions
        fields = ['title', 'content', 'email',]