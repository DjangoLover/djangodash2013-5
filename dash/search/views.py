from django.core.urlresolvers import reverse
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

    if request.method == "POST":

        form = SearchForm()

        if form.is_valid():
            return HttpResponse("Success")

    form = SearchForm()

    return render(request, 'search/search_main.html', {'form': form })
