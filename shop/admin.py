from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name', 'price', 'stock', 'category', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product,ProductAdmin)

class VariationsAdmin(admin.ModelAdmin):
    list_display=("color","size")

admin.site.register(Variation,VariationsAdmin)