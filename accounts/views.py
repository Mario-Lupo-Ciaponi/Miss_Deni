from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from common.mixins import SearchFormMixin
from .forms import UserRegistrationForm, CustomLoginForm


UserModel = get_user_model()


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "registration/registration-form.html"
    success_url = reverse_lazy("login")


class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm


class SearchParentView(SearchFormMixin, ListView):
    model = UserModel
    template_name = "accounts/search-parent.html"
    context_object_name = "parents"
    extra_context = {
        "current_page": "teacher",
    }


    def get_queryset(self):
        parents = UserModel.objects.filter(is_superuser=False)

        search_value = self.request.GET.get("query")

        search_query = Q(username__icontains=search_value) if search_value else Q()

        parents = parents.filter(search_query)

        return parents
