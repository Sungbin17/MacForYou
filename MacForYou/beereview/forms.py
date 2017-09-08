from django import forms
from .models import BeerReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = BeerReview
        fields = ['overall_score', 'comment']