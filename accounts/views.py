from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserRegistrationForm


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration/registration-form.html"
    success_url = reverse_lazy("login")
