from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import SearchForm

class HomePageSearchFormView(FormView):
    template_name = 'pages/home.html'
    form_class = SearchForm

class MainSearchFormView(FormView):
    template_name = 'search/search_main.html'
    form_class = SearchForm

    def form_valid(self, form):
        print 'foo'
        return super(MainSearchFormView, self).form_valid(form)

    def form_invalid(self, form):
        print 'bar'

def main_search_form(request):

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        return render(request, 'search/search_results.html',
            {'query': q} )
    else:
        form = SearchForm()
        messages.warning(request, 'Please enter either a zipcode, city and state, or musical style to find')
        return render(request, 'search/search_main.html', {'form': form })
