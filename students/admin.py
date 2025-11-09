from django.contrib import admin

from .models import Student, Visit, Group


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ...

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    ...
