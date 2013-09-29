import re

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from music.models import MusicProfile
from users.models import User

from .forms import SearchForm
from .utils import do_find, parse_search

class HomePageSearchFormView(FormView):
    template_name = 'pages/home.html'
    form_class = SearchForm

def main_search_form(request):

    if request.GET.items():

        form = SearchForm(request.GET)

        if form.is_valid():

            q = form.cleaned_data['q']
            search_terms = parse_search(q)

            profiles = do_find(request.user, q)

            # some demo data
            if settings.DUMMY_DATA:
                try:
                    dummy_user = User.objects.get(username="tom012345")
                    dummy_profile = MusicProfile.objects.get(user=dummy_user)
                    if dummy_profile:
                        profiles.append(dummy_profile)
                except:
                    pass

            return render(request, 'search/search_results.html',
                {
                    'profiles': profiles,
                    'search_terms': search_terms
                }
            )
    else:
        form = SearchForm()

    return render(request, 'search/search_main.html', {'form': form })


