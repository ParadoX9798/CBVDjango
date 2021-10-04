from django import forms


class TodoCreateForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
