# app_auth/views.py
from django import forms
from django.shortcuts import render
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.views import generic as views
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(auth_forms.UserCreationForm):
    content = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat Password"),
    )
class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm



class LoginUserView(views.View):
    pass


class LogoutUserView(views.View):
    pass
