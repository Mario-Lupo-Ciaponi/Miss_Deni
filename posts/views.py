from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Post
from .choices import PostTypeChoices
from .forms import AddPostModelForm


class NewsListView(ListView):
    model = Post
    template_name = "posts/post-section.html"
    extra_context = {
        "title": "новини",
    }

    def get_queryset(self):
        news = Post.objects.filter(type_of_post=PostTypeChoices.NEWS)

        return news



class AddPostView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = AddPostModelForm
    model = Post
    template_name = "posts/add-post.html"
    success_url = reverse_lazy("index")

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def test_func(self) -> bool:
        return (
            self.request.user.is_superuser
        )
