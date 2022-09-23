from django.shortcuts import render

from .models import producet

def shop(request):
  
  products = producet.objects.all().order_by('pk')
  return render(
    request,
    'shop/shop_index.html',
    {
      'products' : products
      
    }
  )
  
def shop_detail(request):
  return render(
    request,
    'shop/detail.html',
  )  
  