# admin.py

from django.contrib import admin
from .models import Product, Image  # Adjust import as per your project structure

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_code', 'category', 'manufacturer', 'price')
    search_fields = ('title', 'product_code', 'manufacturer')
    list_filter = ('category', 'manufacturer')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('url', 'product')
    search_fields = ('url', 'product__title')
    list_filter = ('product__title',)
