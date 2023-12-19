from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

#for image
import os
def category_banner_upload_to(instance,filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    # Generate a new file name using the category title
    new_filename = f"{instance.title}_{filename}.{ext}"
    # Return the complete file path
    return os.path.join('photo/category', new_filename)

class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = 
    True, null=True)
    title = models.CharField(max_length=100) 
    slug = models.SlugField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    category_baner=models.ImageField(upload_to=category_banner_upload_to,null=True)

    def __str__(self):
        return self.title

    class Meta:

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])