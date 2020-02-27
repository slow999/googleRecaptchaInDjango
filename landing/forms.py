# python import
import requests

# django import
from django import forms
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm


class PasswordResetGoogleRecaptchaForm(PasswordResetForm):
    recaptcha = forms.CharField(
        widget=forms.HiddenInput(),
        max_length=1024,
        required=False
    )

    def clean(self):
        cleaned_data = super(PasswordResetGoogleRecaptchaForm, self).clean()
        recaptcha_token = cleaned_data.get('recaptcha')
        recaptcha_data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_token
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=recaptcha_data)
        result = r.json()
        if result.get('success') and result.get('score') > 0.5:
            # client is human
            print(result)
            pass
        else:
            # client is robot
            raise forms.ValidationError('You are robot!')