from django.shortcuts import render

def index(request):
  return render(
    request,
    'blog/index.html',
  )
  
def promotion(request):
    return render(
      request,
      'blog/popup.html',
    )
  