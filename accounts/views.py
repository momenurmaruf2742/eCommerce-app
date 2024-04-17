from django.shortcuts import render
from django.views import View
# Create your views here.
# Home Page
class Index(View):
    def get(self, request):
        activate = 'home'
        # <view logic>
        return render(request,'home/index.html',{'activate':activate})

# class