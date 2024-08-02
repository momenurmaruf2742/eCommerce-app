from django.db import models
from colorfield.fields import ColorField

from category.models import Category
from django.urls import reverse

from django.utils import timezone
from datetime import timedelta
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    review=models.CharField(max_length=255,blank=True)
    price = models.IntegerField()
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=500,blank=True)
    # available_color = models.ForeignKey(VariationColor,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='available_color')
    # available_size = models.ForeignKey(VariationSize,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='available_size')
    # images = models.ImageField(upload_to = 'photo/products')
    stock = models.IntegerField(default=0)

    discount = models.FloatField(default=0.0)
    discounted_price = models.FloatField(default=0.0)
    sell_price = models.FloatField(default=0.0)

    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    
    def is_new(self):
        return self.created_date >= timezone.now() - timedelta(days=3)
    def save(self,*args,**kwargs):
        discounted_price= ((self.price)*(self.discount))/100
        sell_price = (self.price)-(self.discounted_price)

        self.discounted_price=discounted_price
        self.sell_price=sell_price

        super(Product, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    def __str__(self):
        return self.product_name
    
from django.db import models
from django.utils.safestring import mark_safe
    
class Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True
        )
    image = models.ImageField(blank=True,upload_to = 'photo/products')

    def __str__(self):
        return self.product.product_name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


class Variant(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
        )
    size = models.CharField(blank=True,null=True,max_length=100)
    color = ColorField(null=True,default='')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(null=True,blank=True,max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.price = self.product.price
        super(Variant, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.product_name