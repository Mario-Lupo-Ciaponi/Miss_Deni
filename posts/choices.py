from django.db import models

class PostTypeChoices(models.TextChoices):
    NEWS = "N", "News"
    PHOTO = "P", "Photo"
    VIDEO = "V", "Video"