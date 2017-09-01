from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse
from .forms import ReviewForm
# Create your views here.
from .models import Beer, BeerType, Production_Company, BeerReview


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
            return redirect('reviews:review_list')
    else:
        form = ReviewForm()

    context = {
        'form': form
    }
    return render(request, 'beereview/beereview_create.html', context)

def review_edit(request, pk):
    review = get_object_or_404(BeerReview, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES,instance=review)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('reviews:review_detail', pk)
    else :
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
        return redirect('reviews:reviews_detail', pk)
    else:
        review.delete()
        return redirect('reviews:review_list')
