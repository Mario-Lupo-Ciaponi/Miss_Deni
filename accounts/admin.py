from django.contrib import admin

from .models import MissDeniUser

@admin.register(MissDeniUser)
class MissDeniUserAdmin(admin.ModelAdmin):
    pass

