from django.contrib.auth.views import PasswordResetView
from landing.forms import PasswordResetGoogleRecaptchaForm
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == 'GET':
        return HttpResponse('Welcome!')


class PasswordResetGoogleRecaptchaView(PasswordResetView):
    form_class = PasswordResetGoogleRecaptchaForm
