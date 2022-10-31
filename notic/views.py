from urllib import response
from django.shortcuts import get_object_or_404, render
from .models import *
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q
from datetime import date, datetime, timedelta
from django.http import HttpResponse
from django.views.generic.detail import SingleObjectMixin
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage




class NoticListView(ListView):
    model = Notic
    paginate_by = 10
    context_object_name = 'notic_list'        #DEFAULT : <model_name>_list

    #공지사항 리스트 페이징
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

    #공지사항 게시물 검색
    def get_queryset(self):
      search_keyword = self.request.GET.get('q', '')
      search_type = self.request.GET.get('type', '')
      notic_list = Notic.objects.order_by('-id') 
    
      if search_keyword :
        if len(search_keyword) > 1 :
            if search_type == 'all':
                search_notice_list = notic_list.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword))
            elif search_type == 'title':
                search_notice_list = notic_list.filter(title__icontains=search_keyword)    
            elif search_type == 'content':
                search_notice_list = notic_list.filter(content__icontains=search_keyword)    

            return search_notice_list
        else:
            messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
      return notic_list
    
#공지사항 조회수 기능(쿠키이용)
def notic_detail_view(request, pk):
  notic = get_object_or_404(Notic, pk = pk)
  notic_documents = Document.objects.filter(notic=notic)
  notic_images = NoticImage.objects.filter(notic=notic)
  context = { 
             'notic':notic,
             'notic_documents':notic_documents,
             'notic_images': notic_images,
             }
  response = render(request, 'notic/notic_detail.html', context)
  
  
  expire_date, now =datetime.now(), datetime.now()
  expire_date += timedelta(days=1)
  expire_date = expire_date.replace(hour= 0, minute =0, second = 0, microsecond=0)
  expire_date -= now
  max_age = expire_date.total_seconds()
  
  cookie_value = request.COOKIES.get('hitnotic', '_')
  
  if f'_{pk}_' not in cookie_value:
    cookie_value +=f'{pk}_'
    response.set_cookie('hitnotic', value = cookie_value, max_age = max_age, httponly=True)
    notic.hits +=1
    notic.save()
    
  return response






    
  
  