from django import forms

from chosen import forms as chosenforms

from core.lists import *
from .models import MusicProfile

class MusicProfileForm(forms.ModelForm):

    class Meta:
         # Set this form to use the User model.
        model = MusicProfile

        widgets = {
            'instruments': chosenforms.ChosenSelectMultiple(),
            'styles': chosenforms.ChosenSelectMultiple()
        }

        # Constrain fields.
        fields = ('instruments', 'skill_rating', 'styles', 'zipcode',)
