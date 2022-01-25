from django.contrib import admin
from .models import AuthUser


@admin.register(AuthUser)
class Accounts(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'last_login', 'is_active')
