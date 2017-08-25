from django.shortcuts import render, redirect
from .forms import SuggestionModelForm
# Create your views here.

def suggestions_create(request):
    form=SuggestionModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    else:
        form=SuggestionModelForm()
    content={
        'form':form,
    }
    response = render(request, 'suggestions/suggestions_list.html', content)
    return response