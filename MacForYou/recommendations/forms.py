from django import forms
from .models import Recommendations


class RecommendationModelForm(forms.ModelForm):
    class Meta:
        model = Recommendations
        fields = ['title', 'content', 'email',]