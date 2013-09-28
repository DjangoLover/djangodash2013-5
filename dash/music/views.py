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

# Import the model from music/models.py
from .models import MusicProfile

# Import the form from users/forms.py
from .forms import MusicProfileForm


class MusicProfileDetailView(LoginRequiredMixin, DetailView):
    model = MusicProfile

    def get_object(self):
        # Only get the User record for the user making the request
        return MusicProfile.objects.get(user=self.request.user)


class MusicProfileUpdateView(LoginRequiredMixin, UpdateView):

    form_class = MusicProfileForm

    model = MusicProfile

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("music:detail",
                    kwargs={"pk": self.request.user.id})

    def get_object(self):
        # Only get the User record for the user making the request
        return MusicProfile.objects.get(user=self.request.user)
