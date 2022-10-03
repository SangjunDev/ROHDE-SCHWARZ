from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Q

class ShopList(ListView):
  model = Product
  paginate_by = 6
  context_object_name = 'product_list'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      paginator = context['paginator']
      page_numbers_range = 5
      max_index = len(paginator.page_range)

      page = self.request.GET.get('page',1)
    
      current_page = int(page) if page else 1

      start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
      
      end_index = start_index + page_numbers_range
      if end_index >= max_index:
        end_index = max_index

      page_range = paginator.page_range[start_index:end_index]
      context['page_range'] = page_range
      
      search_keyword = self.request.GET.get('q', '')
      search_type = self.request.GET.get('type', '')

      if len(search_keyword) > 1 :
        context['q'] = search_keyword
      context['type'] = search_type

      return context

  def get_queryset(self):
      search_keyword = self.request.GET.get('q', '')
      search_type = self.request.GET.get('type', '')
      product_list = Product.objects.order_by('-id') 
    
      if search_keyword :
        if len(search_keyword) > 1 :
            if search_type == 'all':
                search_product_list = product_list.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword))
            elif search_type == 'title':
                search_product_list = product_list.filter(title__icontains=search_keyword)    
            elif search_type == 'content':
                search_product_list = product_list.filter(content__icontains=search_keyword)    

            return search_product_list
        else:
            messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
      return product_list     
  
  
def ShopDetail(request,name,pk,category):

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
      'option_images' : option_images
  }

  return render( request, 'shop/product_detail.html', context )  
  