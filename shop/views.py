from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import *

from django.http import HttpResponse

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Min, Max
from django.db.models import Q
# Create your views here.

class Shop(View):
    def get(self, request):
        products = Product.objects.all()
        
        # Extract filter parameters from the request
        price_min_str = request.GET.get('price_min', '')
        price_max_str = request.GET.get('price_max', '')
        
        # Clean and convert price values
        try:
            price_min = float(price_min_str.replace('$', '').replace(',', ''))
        except ValueError:
            price_min = None
        
        try:
            price_max = float(price_max_str.replace('$', '').replace(',', ''))
        except ValueError:
            price_max = None
        
        sizes = request.GET.getlist('sizes')
        colors = request.GET.getlist('colors')
        
        # Apply price filter
        if price_min is not None and price_max is not None:
            products = products.filter(variant__price__gte=price_min, variant__price__lte=price_max)
        elif price_min is not None:
            products = products.filter(variant__price__gte=price_min)
        elif price_max is not None:
            products = products.filter(variant__price__lte=price_max)

        # Apply size filter
        if sizes:
            products = products.filter(variant__size__in=sizes)

        # Apply color filter
        if colors:
            products = products.filter(variant__color__in=colors)
            
        # Extract unique sizes, colors, and price ranges from the products
        unique_sizes = set()
        unique_colors = set()
        min_price = products.aggregate(Min('variant__price'))['variant__price__min'] or 0
        max_price = products.aggregate(Max('variant__price'))['variant__price__max'] or 1000

        for product in products:
            variants = Variant.objects.filter(product=product)
            for variant in variants:
                if variant.size:
                    unique_sizes.add(variant.size)
                if variant.color:
                    unique_colors.add(variant.color)
        
        
        # Paginations
        page = request.GET.get('page', 1)
        # Show 9 products per page
        paginator = Paginator(products, 9)  

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        
        
        product_images = {product.id: Image.objects.filter(product=product).first() for product in products}
        activate = 'shop'
        
        # --------categories-------
        # Get the selected category from the GET parameters
        selected_category_id = request.GET.get('category')
        
        if selected_category_id:
            products = Product.objects.filter(category_id=selected_category_id)
        else:
            products = Product.objects.all()

        # Get all categories for sidebar
        categories = Category.objects.all()
        
        context = {
            'activate': activate,
            'products': products,
            'product_images': product_images,
            'sizes': sorted(unique_sizes),
            'colors': sorted(unique_colors),
            'price_min': price_min_str,
            'price_max': price_max_str,
            'min_price': min_price,
            'max_price': max_price,
            'selected_sizes': sizes,
            'selected_colors': colors,
            'categories': categories,
            'selected_category_id': selected_category_id
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