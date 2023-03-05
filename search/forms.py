from django import forms
from setup.tags_to_json import choices

class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)
