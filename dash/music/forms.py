from django import forms

from core.lists import *

from .models import MusicProfile

class MusicProfileForm(forms.ModelForm):

    class Meta:
         # Set this form to use the User model.
        model = MusicProfile

        # Constrain fields.
        fields = ('instruments', 'skill_rating', 'styles', 'zipcode',)
