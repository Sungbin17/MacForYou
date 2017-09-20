from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from allauth.account.forms import LoginForm
from django.forms import ModelForm


from django.contrib.auth import get_user_model
from django import forms

class SignupForm(forms.ModelForm):
    email = forms.CharField(max_length=30, label='email')
    uid = forms.CharField(max_length=30, label='uid')

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.uid = self.cleaned_data['uid']
        user.save()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15




class LoginForm(AuthenticationForm):
    pass


