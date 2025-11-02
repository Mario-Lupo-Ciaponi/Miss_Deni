from django.urls import reverse_lazy


class IsSuperUserMixin:
    def test_func(self) -> bool:
        return (
            self.request.user.is_superuser
        )


class PostFormMixin:
    template_name = "posts/post-form.html"
    success_url = reverse_lazy("index")
