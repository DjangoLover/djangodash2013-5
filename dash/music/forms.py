from django import forms

from .models import MusicProfile


class MusicProfileForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = MusicProfile

        # Constrain the UserForm to just these fields.
        fields = ('instruments', 'zipcode',)
