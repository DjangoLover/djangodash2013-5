import re

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import SearchForm
from .utils import do_find

class HomePageSearchFormView(FormView):
    template_name = 'pages/home.html'
    form_class = SearchForm

def main_search_form(request):

    if request.GET.items():

        form = SearchForm(request.GET)

        if form.is_valid():

            q = form.cleaned_data['q']

            users = do_find(request.user, q)

            return render(request, 'search/search_results.html',
                {
                    'users': users,
                    'search_string': q
                }
            )
    else:
        form = SearchForm()

    return render(request, 'search/search_main.html', {'form': form })


