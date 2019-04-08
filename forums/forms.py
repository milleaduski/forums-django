from django import forms


class CommentForm(forms.Form):
    desc = forms.CharField(widget=forms.Textarea)
