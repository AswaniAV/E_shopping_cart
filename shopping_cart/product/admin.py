from django.contrib import admin
from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'priority', 'created_at', 'updated_at')
    search_fields = ('title', 'desc')
    list_filter = ('created_at', 'updated_at')
    ordering = ('priority', 'created_at')

admin.site.register(Products, ProductsAdmin)

