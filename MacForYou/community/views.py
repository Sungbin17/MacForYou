from django.shortcuts import redirect, get_object_or_404, render
from .models import Party, Choice, Likes
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from .forms import PartyModelForm, ChoiceModelForm
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json


# Create your views here.

def party_view(request):
	party_list = Party.objects.order_by('-pub_date')[:]
	context = {'party_list': party_list}
	response = render(request, 'community/party_list.html', context)
	return response



def party_detail(request, party_id):
	choice = Choice.objects
	try:
		party = Party.objects.get(pk=party_id)
	except Party.DoesNotExist:
		raise Http404("Party does not exist")
	return render(request, 'community/party_detail.html', {'party': party})

def vote(request, party_id):
	party = get_object_or_404(Party, pk=party_id)
	try:
		selected_choice = party.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'community/party_detail.html', {
			'party': party,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('community:results', args=(party.id,)))

def results(request, party_id):
	party = get_object_or_404(Party, pk=party_id)
	return render(request, 'community/results.html', {'party': party})

def party_create(request):
	form=PartyModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("/community/choice_create")
	else:
		form=PartyModelForm()
	content={
		'form':form,
	}
	response = render(request, 'community/party_form.html', content)
	return response

def choice_create(request):
	form=ChoiceModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("/community/")
	else:
		form=ChoiceModelForm()
	content={
		'form':form,
	}
	response = render(request, 'community/choice_form.html', content)
	return response

@login_required # TODO: Ajax로 처리하기
def party_likes(request, pk):
    party = get_object_or_404(Party, pk=pk)
    # 중간자 모델 Like 를 사용하여, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다.
    post_likes, post_likes_created = party.likes_set.get_or_create(user=request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


