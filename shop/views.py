from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator  

def ShopCategory(request, slug):
  
  category = Category.objects.get(slug=slug)
  product = Product.objects.filter(category=category).order_by('-pk')
  page = request.GET.get('page', '1')  # 페이지
  paginator = Paginator(product, 6)  # 페이지당 10개씩 보여주기
  page_obj = paginator.get_page(page)
  contenxt = {
      'product_list':page_obj,
      'category_list': Category.objects.all(),
      'category': category,
      'page' : page,
      'newCategory':newCategory.objects.all(),
  }
  
  return render(request,'shop/product_list.html',contenxt)

  
def ShopDetail(request,pk,category,name):

  product = Product.objects.get(pk=pk)
  product_images = ProductImage.objects.filter(product=product)
  info_images = InfoImage.objects.filter(product=product)
  spec_images = SpecImage.objects.filter(product=product)
  option_images = OptionImage.objects.filter(product=product)

  context = {
      'product_list' : product,
      'product_images' : product_images,
      'info_images' : info_images,
      'spec_images' : spec_images,
      'option_images' : option_images,
  }

  return render( request, 'shop/product_detail.html', context )  
  

