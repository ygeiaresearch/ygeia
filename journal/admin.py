from django.contrib import admin

from .models import PageType

@admin.register(PageType)
class PageTypeAdmin(admin.ModelAdmin):
    pass