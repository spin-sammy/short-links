from django import forms


class SourceLinkForm(forms.Form):
    source_link = forms.URLField(label='Исходная ссылка (например: https://anc.ua)', widget=forms.TextInput(attrs={'class': 'form-control'}))
