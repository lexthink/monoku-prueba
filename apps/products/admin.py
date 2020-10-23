from django.contrib import admin
from .models import Product, Option


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name', 'description']


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'description']
    search_fields = ['description']
