from django.shortcuts import redirect, get_object_or_404, render
from .models import Meetup, Mlike
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.template import *
from .forms import MeetupModelForm
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models 
import datetime
# Create your views here.

def meetup_view(request):
	#party_list = Party.objects.order_by('-date_meetup')[:]

	meetup_list = Meetup.objects.filter(date_meetup__gte = datetime.date.today())
	#TO_DO: need to sort out like based order

	context = {'meetup_list': meetup_list}

	return render(request, 'community_cardlist.html', context)


def meetup_detail(request, meetup_id):
	meetup = get_object_or_404(Meetup, pk=meetup_id)
	# return render(request, 'community/party_detail.html', {'meetup': meetup})
	return render(request, 'community_detail.html', {'meetup': meetup})


def vote(request, party_id):
	party = get_object_or_404(Meetup, pk=party_id)
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

'''def results(request, party_id):
	party = get_object_or_404(Party, pk=party_id)
	return render(request, 'community/results.html', {'party': party})'''

@login_required
def party_create(request):
	form=MeetupModelForm(request.POST or None, request.FILES or None)

	if request.method == 'POST':
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			return redirect('community:meetups')
	else:
		form=MeetupModelForm()
		content={
			'form':form,
		}	
		# return render(request, 'community/party_form.html', content)
		return render(request, 'community_ce2.html', content)

'''def choice_create(request):
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
	return response'''

@login_required # TODO: Ajax로 처리하기
def party_likes(request, pk):
    party = get_object_or_404(Party, pk=pk)
    # 중간자 모델 Like 를 사용하여, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다.
    post_likes, post_likes_created = party.likes_set.get_or_create(user=request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def home(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }