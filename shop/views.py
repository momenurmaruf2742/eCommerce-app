from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import *

from django.http import HttpResponse
# Create your views here.

class Shop(View):
    def get(self, request):
        products = Product.objects.all()
        product_images = {product.id: Image.objects.filter(product=product).first() for product in products}
        activate = 'shop'
        context={
            'activate':activate,
            'products':products,
            'product_images':product_images,
        }
        # <view logic>
        return render(request,'shop/shop.html',context)

def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        images = Image.objects.filter(product=single_product)
        variants = Variant.objects.filter(product=single_product)
        related_products = Product.objects.filter(category=single_product.category).exclude(id=single_product.id)[:4]
        
    except Exception as e:
        raise e
    context={
        'single_product':single_product,
        'images':images,
        'variants':variants,
        'related_products':related_products

    }
    print(context,"afsddddkjjjjjjjjjjjjjjjjjjjjjjjjj")
    return render(request,'shop/product_details.html',context)