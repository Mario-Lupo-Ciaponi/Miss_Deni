from django.db import models
from accounts.models import MissDeniUser


class Student(models.Model):
    first_name = models.CharField(
        max_length=150,
    )
    last_name = models.CharField(
        max_length=150,
    )
    age = models.PositiveIntegerField()
    parent = models.ForeignKey(
        to=MissDeniUser,
        related_name="children",
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        to="Group",
        related_name="students",
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Visit(models.Model):
    date = models.DateTimeField(
        auto_now_add=True,
    )

    student = models.ForeignKey(
        to=Student,
        related_name="visits",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Присъствал {self.student} на {self.date.strftime('%Y-%m-%d %H:%M')}"


class Group(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return f"Група - {self.name}"
