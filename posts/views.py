from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Post
from .choices import PostTypeChoices
from .forms import AddPostModelForm, EditPostModelForm
from .mixins import IsSuperUserMixin


class NewsListView(ListView):
    model = Post
    template_name = "posts/post-section.html"
    extra_context = {
        "title": "новини",
    }

    def get_queryset(self):
        news = Post.objects.filter(type_of_post=PostTypeChoices.NEWS).order_by("-posted_on")

        return news


class NormalPostListView(ListView):
    model = Post
    template_name = "posts/post-section.html"
    extra_context = {
        "title": "публикации",
    }

    def get_queryset(self):
        posts = Post.objects.filter(type_of_post=PostTypeChoices.NORMAL_POST).order_by("-posted_on")

        return posts



class AddPostView(LoginRequiredMixin, IsSuperUserMixin, UserPassesTestMixin, CreateView):
    form_class = AddPostModelForm
    model = Post
    template_name = "posts/post-form.html"
    success_url = reverse_lazy("index")
    extra_context = {
        "title": "Създай Публикация"
    }


class EditPostView(LoginRequiredMixin, UpdateView):
    form_class = EditPostModelForm
    model = Post
    template_name = "posts/post-form.html"
    success_url = reverse_lazy("index")
    extra_context = {
        "title": "Промени Публикация"
    }


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/confirm-delete.html"
    success_url = reverse_lazy("index")

