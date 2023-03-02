from django import forms
from setup.tags_to_json import choices


class CreatePost(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    tags = forms.ChoiceField(choices=choices)
    
