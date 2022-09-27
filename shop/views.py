from django.views.generic import ListView, DetailView
from .models import *

class ShopList(ListView):
  model = Product
  ordering = '-pk'
  
class ShopDetail(DetailView):
  model = Product  



#def shop_index(request):
  
#  products = Product.objects.all().order_by('pk')
#  return render(
#    request,
#    'shop/shop_index.html',
#    {
#      'products' : products
      
#    }
#  )
  
#def shop_detail(request):
#  return render(
#    request,
#    'shop/detail.html',
#  )  
  