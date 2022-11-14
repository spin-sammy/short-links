from django import forms


class SourceLinkForm(forms.Form):
    source_link = forms.URLField(label='Вихідне посилання (наприклад: https://anc.ua)',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
