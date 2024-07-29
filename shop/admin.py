from django.contrib import admin
from .models import *
# Register your models here.


# admin.site.register(Image)
# admin.site.register(Variant)
class ProductImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('id', 'image_tag',)
    extra = 1
    
class ProductVariantInline(admin.TabularInline):
    model = Variant
    readonly_fields = ('id',)
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name', 'price', 'stock', 'category', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    readonly_fields = ('discounted_price','sell_price')
    inlines=(ProductImageInline,ProductVariantInline)

admin.site.register(Product,ProductAdmin)
