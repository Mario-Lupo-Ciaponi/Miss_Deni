from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from common.mixins import SearchFormMixin
from .models import Post
from .choices import PostTypeChoices
from .forms import AddPostModelForm, EditPostModelForm
from .mixins import  PostFormMixin
from common.mixins import IsSuperUserMixin


class NewsListView(SearchFormMixin, ListView):
    model = Post
    template_name = "posts/post-section.html"
    extra_context = {
        "title": "новини",
        "current_page": "news",
    }

    def get_queryset(self):
        news = Post.objects.filter(type_of_post=PostTypeChoices.NEWS).order_by("-posted_on")

        search_value = self.request.GET.get("query")

        search_query = Q(title__icontains=search_value) if search_value else Q()

        news = news.filter(search_query)

        return news


class NormalPostListView(SearchFormMixin, ListView):
    model = Post
    template_name = "posts/post-section.html"
    extra_context = {
        "title": "публикации",
        "current_page": "normal_post",
    }

    def get_queryset(self):
        posts = Post.objects.filter(type_of_post=PostTypeChoices.NORMAL_POST).order_by("-posted_on")

        search_value = self.request.GET.get("query")

        search_query = Q(title__icontains=search_value) if search_value else Q()

        posts = posts.filter(search_query)

        return posts



class AddPostView(LoginRequiredMixin, IsSuperUserMixin, UserPassesTestMixin, PostFormMixin, CreateView):
    form_class = AddPostModelForm
    model = Post
    extra_context = {
        "title": "Създай Публикация",
        "current_page": "teacher",
    }


class EditPostView(LoginRequiredMixin, IsSuperUserMixin, UserPassesTestMixin, PostFormMixin, UpdateView):
    form_class = EditPostModelForm
    model = Post
    extra_context = {
        "title": "Промени Публикация"
    }


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/confirm-delete.html"
    success_url = reverse_lazy("index")

