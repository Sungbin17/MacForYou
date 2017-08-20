from django.shortcuts import render, redirect
from .forms import RecommendationModelForm
# Create your views here.

def recommendation_create(request):
    form=RecommendationModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/post/")
    else:
        form=RecommendationModelForm()
    content={
        'form':form,
    }
    response = render(request, 'recommendation/recommendation_list.html', content)
    return response