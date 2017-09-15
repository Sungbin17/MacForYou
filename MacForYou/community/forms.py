from django import forms
from .models import Meetup
from django.forms import DateTimeField
from datetimewidget.widgets import DateTimeWidget


class MeetupModelForm(forms.ModelForm):
    class Meta:
        model = Meetup
        fields = ['title', 'content', 'place', 'kakao_open_chat_link', 'date_meetup' ]
       	widgets = {
            'date_meeting': forms.DateTimeInput(),
        }

# class ChoiceModelForm(forms.ModelForm):
#     class Meta:
#         model = Choice
#         fields = ['party', 'choice_text',]




