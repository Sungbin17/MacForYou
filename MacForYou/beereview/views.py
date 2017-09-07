from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Beer, BeerType, Production_Company, BeerReview
import random


# ClassBaseView

class BeerDetailView(DetailView):
    template_name = 'beer_detail.html'

    def get_object(self, *args, **kwargs):
        name = self.kwargs.get("slug")
        instance = get_object_or_404(Beer, name__iexact=name)  # iexact make nonecase sensetive db search
        return instance

    def get_context_data(self, *args, **kwargs):
        context = super(BeerDetailView, self).get_context_data(*args, **kwargs)
        context['beer_reviews'] = context['object'].beer_reviews.all()
        return context


class BeerTypeDetailView(DetailView):
    template_name = 'beertype_detail.html'

    def get_object(self, *args, **kwargs):
        name = self.kwargs.get("slug")
        instance = get_object_or_404(BeerType, name__iexact=name)  # iexact make nonecase sensetive db search
        return instance

    def get_context_data(self, *args, **kwargs):
        context = super(BeerTypeDetailView, self).get_context_data(*args, **kwargs)
        context['beertype_beers_list'] = context['object'].beertype_beers.all()

        return context


# class BeerTypeDetailView(View):
# 	def get(self, request, *args, **kwargs):
# 		name = 'lager'
# 		instance = get_object_or_404(BeerType, name__iexact=name)
# 		print(instance.beertype_beers.all())
# 		return HttpResponse('debuging')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'index.html', context)

class BeerListView(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request, 'beer_list.html', context)










def beer_type(request, slug):
    beer_type = get_object_or_404(BeerType, name__iexact=slug)

    related_beers = Beer.objects.filter(name__iexact=slug)
    related_reviews = BeerReview.objects.select_related('beer__beertype').filter(beer__beertype__name__iexact=slug).order_by('-updated') # 관련 리뷰 업데이트순으로


    recom_type = BeerType.objects.exclude(name__iexact=slug)
    # 현재 접근한 타입을 제외한 다른 모든 타입을 가져온뒤

    recom_idx = []
    for recom in recom_type:
        recom_idx.append(recom.id)
    recom_idx = random.sample(recom_idx, 3)
    #랜덤함수를 이용하여 인덱스를 임의로 3개 뽑고 recom_idx에 저장

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
    beer = get_object_or_404(Beer, name__iexact=slug)
    review_list = BeerReview.objects.filter(beer_id=beer.id)
    recom_beers = Beer.objects.exclude(name__iexact=slug).order_by('-updated')[:3]


    score_full = round(beer.abv, 2) # 값이 하나기때문에 뷰에서 반올림
    score_star = round(beer.abv)


    # TODO 쿼리셋을 분해해서 js 오브젝트처럼 값넣기
    modifiable = []
    for review in review_list:

        if (request.user.id != review.user_id):
            modifiable.append(False)

        else:
            modifiable.append(True)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('beers:beer_detail', slug)

    else:
        form = ReviewForm()

    context = {
        'form': form,
        'beer': beer,
        'beer_score_full': score_full,
        'beer_score_star': score_star,

        'review_list': review_list,
        'review_modifiable': modifiable,
        'recom_beers':recom_beers,
    }

    # return render(request, 'beereview/beer_detail2.html', context)
    return render(request, 'beer_detail.html', context)


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


def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('beers:review_list')
    else:
        form = ReviewForm()

    context = {
        'form': form
    }
    return render(request, 'beereview/beereview_create.html', context)


def review_edit(request, pk):
    review = get_object_or_404(BeerReview, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('beers:review_detail', pk)
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


def review_delete(request, pk):
    review = get_object_or_404(BeerReview, pk=pk)

    if review.user_id != request.user.id:
        return redirect('beers:reviews_detail', pk)
    else:
        review.delete()
        return redirect('beers:review_list')
