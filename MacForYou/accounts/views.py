from django.http import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from .forms import UserForm, LoginForm, SignupForm
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.contrib.auth.models import User
from .models import UserProfiles
# Create your views here.

def signup(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user2 = UserProfiles(user=new_user, score=0, number_of_posts=0).save()
            auth_login(request, new_user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return HttpResponse('사용자명이 이미 존재합니다.')
    else:
        form=SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form':form,
        })

@login_required
def profile(request):
    return render(request,'accounts/profile.html')

def login(request):
    providers = []
    for provider in get_providers():
        # social_app 속성은 provider에는 없는 속성입니다.
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)
    return auth_login(request,
        authentication_form=LoginForm,
        template_name='accounts/login_form.html',
        extra_context={'providers': providers})

def userrank(request):
    userrank = User.objects.all()
    userrank2= UserProfiles.objects.all()
    ctx = {
        'user': userrank, 'user2':userrank2
    }
    return render(request, 'accounts/userrank.html', ctx)
