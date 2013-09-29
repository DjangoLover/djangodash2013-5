from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class SearchForm(forms.Form):

    search_field = forms.CharField(max_length=50, help_text='Enter up to 50 characters maximum.')

    def clean_search_field(self):

        return self.cleaned_data['search_field']
