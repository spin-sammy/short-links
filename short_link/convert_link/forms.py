from django import forms


class SourceLinkForm(forms.Form):
    source_link = forms.CharField(label='Source link', widget=forms.TextInput(attrs={'class': 'form-control'}))
