from django.shortcuts import render, redirect
from .models import Party
# Create your views here.

def Party_view(request):
    party_list = Party.objects.order_by('-pub_date')[:]
    context = {'party_list': party_list}
    response = render(request, 'community/party_list.html', context)
    return response