# -*- coding: utf-8 -*-
# Import the reverse lookup function
from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from pyzipcode import ZipCodeDatabase

from users.models import User
from .models import MusicProfile
from .forms import MusicProfileForm


class MusicProfileDetailView(LoginRequiredMixin, DetailView):
    model = MusicProfile
    slug_field = "pk"
    slug_url_kwarg = "pk"

class MusicProfileSelfDetailView(LoginRequiredMixin, DetailView):
    model = MusicProfile

    def get_object(self):
        # Only get the User record for the user making the request
        return MusicProfile.objects.get(user=self.request.user)


    def get_context_data(self, **kwargs):
        context = super(MusicProfileSelfDetailView, self).get_context_data(**kwargs)
        zip = self.object.zipcode
        zcdb = ZipCodeDatabase()
        zip_obj = zcdb[zip]
        context['zipcode'] = {'city': zip_obj.city, 'state': zip_obj.state}

        return context

class MusicProfileUpdateView(LoginRequiredMixin, UpdateView):

    form_class = MusicProfileForm

    model = MusicProfile

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("music:self_detail")

    def get_object(self):
        # Only get the User record for the user making the request
        return MusicProfile.objects.get(user=self.request.user)
