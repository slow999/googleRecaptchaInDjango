from django.urls import path
from landing import views

app_name = 'landing'


urlpatterns = [
    path('password_reset/', views.PasswordResetGoogleRecaptchaView.as_view(), name='password_reset')
]