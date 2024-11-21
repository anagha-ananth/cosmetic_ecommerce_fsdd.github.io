# admin.py
from django.contrib import admin
from .models import Product, Cart, Wishlist

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'image')
    search_fields = ('name',)
    
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)
