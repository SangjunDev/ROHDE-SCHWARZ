from django.shortcuts import render

from .models import oscillo

def shop_Osciiloscope(request):
  
  products = oscillo.objects.all().order_by('pk')
  return render(
    request,
    'shop/shop_Osciiloscope.html',
    {
      'products' : products
      
    }
  )
  
def shop_detail(request):
  return render(
    request,
    'shop/detail.html',
  )  
  