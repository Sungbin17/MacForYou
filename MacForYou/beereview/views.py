from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Beer, BeerType, Production_Company, BeerReview
import random

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# ClassBaseView

# class BeerDetailView(DetailView):
#     template_name = 'beer_detail.html'

#     def get_object(self, *args, **kwargs):
#         name = self.kwargs.get("slug")
#         instance = get_object_or_404(Beer, name__iexact=name)  # iexact make nonecase sensetive db search
#         return instance

#     def get_context_data(self, *args, **kwargs):
#         context = super(BeerDetailView, self).get_context_data(*args, **kwargs)
#         context['beer_reviews'] = context['object'].beer_reviews.all()
#         return context


# class BeerTypeDetailView(DetailView):
#     template_name = 'beertype_detail.html'

#     def get_object(self, *args, **kwargs):
#         name = self.kwargs.get("slug")
#         instance = get_object_or_404(BeerType, name__iexact=name)  # iexact make nonecase sensetive db search
#         return instance

#     def get_context_data(self, *args, **kwargs):
#         context = super(BeerTypeDetailView, self).get_context_data(*args, **kwargs)
#         context['beertype_beers_list'] = context['object'].beertype_beers.all()

#         return context

# class BeerTypeDetailView(View):
# 	def get(self, request, *args, **kwargs):
# 		name = 'lager'
# 		instance = get_object_or_404(BeerType, name__iexact=name)
# 		print(instance.beertype_beers.all())
# 		return HttpResponse('debuging')


def index_view(request):
    context_object = []
    recent_beereview = BeerReview.objects.select_related('beer', 'user').order_by('-created')[:4]

    for beereview in recent_beereview:
        append_beereview = beereview
        append_user = beereview.user
        append_beer = beereview.beer

        append_context = { 
            'beereview'     : append_beereview,
            'review_user'   : append_user,
            'review_beer'   : append_beer,
        }
        
        context_object.append(append_context)
        print(context_object)
    context = {
        'recents_reviews': context_object
    }
    return render(request, 'index.html', context)




def beer_type(request, slug):

    beer_type = get_object_or_404(BeerType, name__iexact=slug)

    # related_beers = Beer.objects.filter(name__iexact=slug)
    related_beers = Beer.objects.select_related('beertype').filter(beertype__name__iexact=slug)
    related_reviews = BeerReview.objects.select_related('beer__beertype').filter(
        beer__beertype__name__iexact=slug).order_by('-updated')  # 관련 리뷰 업데이트순으로

    recom_type = BeerType.objects.exclude(name__iexact=slug)
    # 현재 접근한 타입을 제외한 다른 모든 타입을 가져온뒤

    recom_idx = []
    for recom in recom_type:
        recom_idx.append(recom.id)
    recom_idx = random.sample(recom_idx, 2)
    # 랜덤함수를 이용하여 인덱스를 임의로 3개 뽑고 recom_idx에 저장

    recom_type = BeerType.objects.filter(pk__in=recom_idx)
    # 랜덤으로 인덱스를 가져와서 그 값에 해당한 타입을 가져옴

    context = {
        'beer_type': beer_type,
        'related_beers': related_beers,
        'related_reviews': related_reviews,
        'recom_types': recom_type,
    }

    # return render(request, 'beereview/beer_type.html', context)
    return render(request, 'beertype_detail.html', context)


def beer_detail(request, slug):
    #TODO : diff my review and others
    beer = get_object_or_404(Beer, name__iexact=slug)
    review_list = BeerReview.objects.filter(beer_id=beer.id)
    recom_beers = Beer.objects.exclude(name__iexact=slug).order_by('-updated')[:3]

    page = request.GET.get('page', 1)
    paginator = Paginator(review_list, 10)

    try:
        paged_reviews = paginator.page(page)
    except PageNotAnInteger:
        paged_reviews = paginator.page(1)
    except EmptyPage:
        paged_reviews = paginator.page(paginator.num_pages)

    # TODO 쿼리셋을 분해해서 js 오브젝트처럼 값넣기
    modifiable = []
    for review in review_list:

        if (request.user.id != review.user_id):
            modifiable.append(False)

        else:
            modifiable.append(True)

    context = {
        'beer': beer,

        # 'review_list': review_list,
        'paged_reviews': paged_reviews,
        'review_modifiable': modifiable,
        'recom_beers': recom_beers,
    }

    #return render(request, 'beereview/beer_detail2.html', context)
    return render(request, 'beer_detail.html', context)


def beers_list(request):
    beers = Beer.objects.order_by('-overall_score')[:20]
    # print(beers)
    context = {
        'beer_list': beers
    }
    return render(request, 'beer_list.html', context)


def review_list(request):
    reviews = BeerReview.objects.filter()
    context = {
        'reviews': reviews
    }
    return render(request, 'beereview/beereview_list.html', context)


def review_detail(request, pk):
    review = get_object_or_404(BeerReview, pk=pk)
    context = {
        'review': review
    }
    return render(request, 'beereview/beereview_detail.html', context)


@login_required
@transaction.atomic
def review_create(request, slug):
    #purpose of this view is check if one user one review only rule
    #and edit or create at once

    beer = get_object_or_404(Beer, name__iexact=slug)
    first_write_flag = False
    
    try:
        #if user already wrote review then he only edit
        org_review = BeerReview.objects.get( user=request.user, beer=beer.id )

    except ObjectDoesNotExist:
        first_write_flag = True

    if first_write_flag == True:
        send_form = ReviewForm()
    else:
        send_form = ReviewForm(instance=org_review)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            if first_write_flag == False:
                form = ReviewForm(request.POST, request.FILES, instance=org_review)
                beer.reviews_count -=1
                beer.total_sum -= org_review.overall_score

            obj = form.save(commit=False)
            obj.user = request.user
            obj.beer_id = beer.id
           
            beer.reviews_count +=1
            beer.total_sum += obj.overall_score
            beer.overall_score = beer.total_sum / beer.reviews_count

            obj.save()
            beer.save()
            return redirect('beers:beer_detail', slug)

    else:
        # if request is get
        context = {
            'form': send_form,
            'slug': slug
        }
        return render(request, 'beer_review_ce.html', context)


        #user not wrote review before

        # if request.method == 'POST':
    #     form = ReviewForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         obj.user = request.user
    #         obj.beer_id = beer.id
    #         obj.save()

    #         beer.reviews_count +=1
    #         beer.total_sum += obj.overall_score

    #         beer.overall_score = beer.total_sum / beer.reviews_count
    #         beer.save()

    #         return redirect('beers:beer_detail', slug)

    # else:
    #     form = ReviewForm()

    # context = {
    #     'form': form
    # }
    # # return render(request, 'beereview/beereview_create.html', context)
    # context = {}
    # return render(request, 'beer_review_ce.html', context)


def review_edit(request, pk):
    review = get_object_or_404(BeerReview, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('beers:beers_detail', review.beer.name)
    else:
        initial = {
            'overall_score': review.overall_score,
            'beer': review.beer.id,
            'comment': review.comment
        }
        form = ReviewForm(initial=initial)

    context = {
        'form': form,
        'review': review
    }
    return render(request, 'beereview/beereview_edit.html', context)


# def review_delete(request, pk):
#     print('hey')
#     review = get_object_or_404(BeerReview, pk=pk)
#     redirect_name = review.beer.name
#     if request.method == 'POST':
#         if review.user_id == request.user.id:
#             review.delete()
#             # return redirect('beers:beers_list')
#     return redirect('beers:beers_detail', redirect_name)

@login_required
@transaction.atomic
def review_delete(request, slug):
    beer = get_object_or_404(Beer, name__iexact=slug)
    try:
        #if user already wrote review then he only edit
        org_review = BeerReview.objects.get( user=request.user, beer=beer.id )

    except ObjectDoesNotExist:
        return redirect('beers:beers_detail', slug)

    if request.method == 'POST':
        beer.reviews_count -= 1
        beer.total_sum -= org_review.overall_score
        if beer.reviews_count == 0:
            beer.overall_score = 0
            beer.total_sum = 0
        else:
            beer.overall_score = beer.total_sum / beer.reviews_count

        org_review.delete()
        beer.save()
    return redirect('beers:beer_detail', slug)




    review = get_object_or_404(BeerReview, pk=pk)
    redirect_name = review.beer.name
    if request.method == 'POST':
        if review.user_id == request.user.id:
            review.delete()
            # return redirect('beers:beers_list')
    return redirect('beers:beers_detail', redirect_name)


def beer_search(request, slug):
    beers = Beer.objects.filter(name__contains=slug).order_by('-overall_score')

    context = {
        'search_text' : slug,
        'beer_list': beers,
    }
    return render(request, 'beer_search.html', context)
