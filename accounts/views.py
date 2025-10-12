from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserRegistrationForm, CustomLoginForm


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration/registration-form.html"
    success_url = reverse_lazy("login")


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
