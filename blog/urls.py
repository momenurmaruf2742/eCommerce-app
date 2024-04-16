from django.urls import path
from . views import *

urlpatterns = [
    path("", Blog.as_view(),name='blog'),
    path("blog-details/",BlogDetails.as_view(),name='blog-details')
]