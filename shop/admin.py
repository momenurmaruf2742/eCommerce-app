from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name', 'price', 'stock', 'category', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product,ProductAdmin)

class VariationsColorAdmin(admin.ModelAdmin):
    list_display=("name","color")

admin.site.register(VariationColor ,VariationsColorAdmin)

class VariationsSizeAdmin(admin.ModelAdmin):
    list_display=("name","size")

admin.site.register(VariationSize,VariationsSizeAdmin)