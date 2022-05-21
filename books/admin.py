from django.contrib import admin
from .models import Books


# Register your models here.
@admin.register(Books)
class AdminBooks(admin.ModelAdmin):
    list_display = ['id', 'title', 'excerpt']
