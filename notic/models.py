from email.policy import default
from django.db import models
import os
from django.conf import settings


# Create your models here.

class Notic(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    
    title = models.CharField(max_length=128, verbose_name='제목')
    
    content = models.TextField(verbose_name='내용')
    
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'notic'
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항'
        
def document_file_upload_path(instance, filename):
    return f'upload_file/notic/document/{instance.notic.title}/{filename}'

def notic_image_upload_path(instance, filename):
    return f'upload_file/notic/image/{instance.notic.title}/{filename}'               

class Document(models.Model):
  notic = models.ForeignKey(Notic, on_delete=models.CASCADE)
  
    #첨부 파일
  noticdocuments = models.FileField(upload_to=document_file_upload_path, blank=True,null=False, default='',verbose_name='첨부파일')
  
  
class NoticImage(models.Model):
  notic = models.ForeignKey(Notic, on_delete=models.CASCADE)
  
    #제품 사진
  noticimages = models.ImageField(upload_to=notic_image_upload_path, blank=True,null=False, default='',verbose_name='제품 이미지')          

    
