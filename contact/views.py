
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages

def contact(request):
  if request.method == "POST":
    
    
    
    company  = request.POST["company"]
    position = request.POST["position"]
    name = request.POST["name"]
    phone = request.POST["phone"] 
    email = request.POST["email"]
    message=request.POST["message"]
    
    emailContent = render_to_string('contact/email.html',{
      "company":company,
      "position":position,
      "name":name,
      "phone":phone,
      "email":email,
      "message":message}
    )
    
    title = "[로데슈바르즈 문의]"
    emailAdress = "sj.kim@cndi.co.kr"
    
    emailObject = EmailMessage(title, emailContent, to =[emailAdress])
    emailObject.content_subtype = "html"
    
    result = emailObject.send()
    
    if result == 1:
      messages.info(request, "성공적으로 접수되었습니다.")  

    else:
      messages.info(request, "접수에 실패하였습니다.")
    
    return redirect('contact')
  
  else:
    
  
    return render(
      request,
      'contact/contact.html',
    )
