from django.shortcuts import render
from django.views.generic import ListView

from .models import Post
from .choices import PostTypeChoices


class NewsListView(ListView):
    model = Post
    template_name = "posts/post-section.html"
    extra_context = {
        "title": "новини",
    }

    def get_queryset(self):
        news = Post.objects.filter(type_of_post=PostTypeChoices.NEWS)

        return news
