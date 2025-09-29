from django.db import models
from .choices import PostTypeChoices

class Post(models.Model):
    title = models.CharField(
        max_length=50,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    file = models.FileField(
        upload_to="posts/",
    )
    type_of_post = models.CharField(
        max_length=5,
        choices=PostTypeChoices.choices,
    )
    posted_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
