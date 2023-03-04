from django import forms
from setup.tags_to_json import choices

class CreatePost(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    tags = forms.ChoiceField(choices=choices)

class EditPost(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    tags = forms.ChoiceField(choices=choices)

    def __init__(self, post, *args, **kwargs):
        super(EditPost, self).__init__(*args, **kwargs)
        self.fields['title']. initial = post.title
        self.fields['body']. initial = post.body

class AnswerPost(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
