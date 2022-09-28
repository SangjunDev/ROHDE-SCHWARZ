from email.policy import default
from django.db import models


class Category(models.Model):
  name = models.CharField(max_length = 50, unique=True, null=True, default='')
  slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, null=True, default='')
    
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = 'Categories'
    
  def get_absolute_url(self):
      return f'/blog/category/{self.slug}/'

class Product(models.Model):

  # 상품명
  name = models.TextField(null=True, default='',verbose_name='상품명')
  # 간단한 설명
  about = models.TextField(null=True,default='',verbose_name='간단한 설명')
  
  #데이터 시트 및 기타 자료 요청
  DataSheet_Etc = models.TextField(null=True,default='',verbose_name='데이터 시트 및 기타 자료')
  
  
  category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, default='' ,verbose_name='카테고리')

  def __str__(self):
    return f'[{self.pk}] {self.name}'
  
  def get_absolute_url(self):
      return f'/shop/{self.name}/{self.pk}'
    
  class Meta:
    db_table = 'product'  

def product_mage_upload_path(instance, filename):
    return f'upload_file/product/main/{instance.product.name}/{filename}'
  
def information_mage_upload_path(instance, filename):
    return f'upload_file/product/information/{instance.product.name}/{filename}'
     
def specification_mage_upload_path(instance, filename):
    return f'upload_file/product/specification/{instance.product.name}/{filename}'

def option_mage_upload_path(instance, filename):
    return f'upload_file/product/option/{instance.product.name}/{filename}'                

class ProductImage(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  
    #제품 사진
  product_Image = models.ImageField(upload_to=product_mage_upload_path, blank=True, default='',verbose_name='메인 이미지')
  
  #제품 설명 사진
  information_Image = models.ImageField(upload_to=information_mage_upload_path, blank=True, default='',verbose_name='설명 이미지')
  
  #제품 사양 사진
  specification_Image = models.ImageField(upload_to=specification_mage_upload_path, blank=True, default='',verbose_name='사양 이미지')
  
  #제품 옵션 사진
  option_Image = models.ImageField(upload_to=option_mage_upload_path, blank=True, default='',verbose_name='옵션 이미지')
      