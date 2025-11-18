from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .models import Group
from .forms import CreateGroupModelForm, UpdateGroupModelForm


class CreateFormView(CreateView):
    model = Group
    form_class = CreateGroupModelForm
    template_name = "students/group-form.html"
    success_url = reverse_lazy("admin-panel")
    extra_context = {
        "title": "Създай група",
        "submit_button_text": "Създай"
    }

class UpdateFormView(UpdateView):
    model = Group
    form_class = UpdateGroupModelForm
    template_name = "students/group-form.html"
    success_url = reverse_lazy("admin-panel")
    extra_context = {
        "title": "Редактирай група",
        "submit_button_text": "Редактирай"
    }
