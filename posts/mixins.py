from django.urls import reverse_lazy


class PostFormMixin:
    template_name = "posts/post-form.html"
    success_url = reverse_lazy("index")
