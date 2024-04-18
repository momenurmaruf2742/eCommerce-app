from django.db import models
from colorfield.fields import ColorField

from category.models import Category
from django.urls import reverse
# Create your models here.


class VariationColor(models.Model):
    name = models.CharField(max_length=50)
    color=ColorField()
    is_active = models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return self.name
class VariationSize(models.Model):
    name = models.CharField(max_length=50)
    size=models.CharField(max_length=3)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    def __str__(self):
        return self.size
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    review=models.CharField(max_length=255,blank=True)
    price = models.IntegerField()
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=500,blank=True)
    available_color = models.ForeignKey(VariationColor,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='available_color')
    available_size = models.ForeignKey(VariationSize,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='available_size')
    images = models.ImageField(upload_to = 'photo/products')
    stock = models.IntegerField()

    discount = models.FloatField(default=0.0)
    discounted_price = models.FloatField(default=0.0)
    sell_price = models.FloatField(default=0.0)

    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
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