from django.contrib import admin
from .models import SliderImages


@admin.register(SliderImages)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')
