from django import forms
from .models import Meetup
from django.forms import DateTimeField


class MeetupModelForm(forms.ModelForm):
    class Meta:
        model = Meetup
        fields = ['title', 'content', 'place', 'kakao_open_chat_link', 'date_meetup' ]

# class ChoiceModelForm(forms.ModelForm):
#     class Meta:
#         model = Choice
#         fields = ['party', 'choice_text',]




