from django.shortcuts import render

from .models import About_Post

def about(request):
  
  # 모든 Post를 가져와 postlist에 저장한다.
  postlist = About_Post.objects.all()
  
  #about.html 페이지를 열때, postlist도 같이 가져온다.
  return render(
    request,
    'about/about.html',
    {'postlist':postlist},
  )
 
  