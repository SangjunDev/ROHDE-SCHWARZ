from enum import unique
from django.db import models

class Category(models.Model):
  name = models.CharField(max_length = 50, unique=True)
  slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = '제품 카테고리'
    
  def get_absolute_url(self):
      return f'/shop/{self.slug}/'    
  



class Product(models.Model):
  # 제품 카테고리
  category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

  # 상품명
  name = models.TextField(blank=False, default='',verbose_name='상품명')
  
  #대표 이미지
  image = models.ImageField(upload_to = 'upload_file', blank=False, default='',verbose_name='메인 이미지')
  
  # 간단한 설명
  about = models.TextField(blank=False,default='',verbose_name='간단한 설명')
  
  #데이터 시트 및 기타 자료 요청
  DataSheet_Etc = models.TextField(blank=False,default='',verbose_name='데이터 시트 및 기타 자료')

  def __str__(self):
    return f'[{self.pk}] {self.name}'
  
  def get_absolute_url(self):
      return f'/shop/{self.category}/{self.name}/{self.pk}'
    
  class Meta:
    db_table = 'product'
    verbose_name = '제품 등록'
    verbose_name_plural = '제품 등록'

def product_image_upload_path(instance, filename):
    return f'upload_file/product/product/{instance.product.name}/{filename}'
  
def information_image_upload_path(instance, filename):
    return f'upload_file/product/information/{instance.product.name}/{filename}'
     
def specification_image_upload_path(instance, filename):
    return f'upload_file/product/specification/{instance.product.name}/{filename}'

def option_image_upload_path(instance, filename):
    return f'upload_file/product/option/{instance.product.name}/{filename}'       
    
class ProductImage(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  
    #제품 사진
  productimages = models.ImageField(upload_to=product_image_upload_path, blank=False, default='',verbose_name='제품 이미지')
  
class InfoImage(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  
  #제품 설명 사진
  informationimages = models.ImageField(upload_to=information_image_upload_path, blank=False, default='',verbose_name='설명 이미지')
  
class SpecImage(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  #제품 사양 사진
  specificationimages = models.ImageField(upload_to=specification_image_upload_path, blank=False, default='',verbose_name='사양 이미지')
  
class OptionImage(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)      
  #제품 옵션 사진
  optionimages = models.ImageField(upload_to=option_image_upload_path, blank=False, default='',verbose_name='옵션 이미지')
      