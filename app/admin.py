from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "upload_date")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog, BlogAdmin)