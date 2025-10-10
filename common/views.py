from http.client import HTTPResponse

from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ContactForm


def index_view(request: HttpRequest) -> HTTPResponse:
    return render(request, "index.html")


def about_view(request: HttpRequest) -> HTTPResponse:
    return render(request, "common/about.html")


class ContactView(FormView):
    form_class = ContactForm

    template_name = "common/contact.html"
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        print("yes")

        return super().form_valid(form)
