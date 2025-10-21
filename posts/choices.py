from django.db import models

class PostTypeChoices(models.TextChoices):
    NEWS = "N", "Новини"
    PHOTO = "P", "Снимка"
    NORMAL_POST = "V", "Нормална публиация"