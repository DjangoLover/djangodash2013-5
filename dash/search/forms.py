from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class SearchForm(forms.Form):

    q = forms.CharField(
        max_length=50,
        help_text='Enter up to 50 characters maximum.',
        label="Search",
        widget=forms.TextInput(attrs={'placeholder': 'Enter a Zipcode, City and State'}))

    def clean_q(self):
        q = self.cleaned_data['q']

        if not q:
            raise FormValidation('You must enter one search term')

        return q
