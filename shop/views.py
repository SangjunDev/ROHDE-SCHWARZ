from django.shortcuts import render

def shop(request):
  return render(
    request,
    'shop/shop_index.html',
  )
  
def shop_detail(request):
  return render(
    request,
    'shop/detail.html',
  )  
  