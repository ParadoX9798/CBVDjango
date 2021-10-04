from django import forms
from .models import Comment


class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body",)
