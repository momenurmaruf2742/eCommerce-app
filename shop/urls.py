from django.urls import path
from . views import *

urlpatterns = [
    path("", Shop.as_view(),name='shop'),
    path('shop/<slug:category_slug>/<slug:product_slug>',product_detail,name='product_detail'),
]