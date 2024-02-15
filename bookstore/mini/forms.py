from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class MyForm(forms.Form):
    url = forms.CharField(label='URL')

    def clean_url(self):
        url = self.cleaned_data['url']
        validate_url = URLValidator()
        try:
            validate_url(url)
        except ValidationError as e:
            raise forms.ValidationError("Invalid URL") from e
        return url