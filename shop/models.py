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
  name = models.TextField(null=True, default='')
  # 간단한 설명
  about = models.TextField(null=True,default='')
  
  #데이터 시트 및 기타 자료 요청
  DataSheet_Etc = models.TextField(null=True,default='')
  
  
  category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, default='')
  
  def __str__(self):
    return f'[{self.pk}] {self.name}'
  
  def get_absolute_url(self):
      return f'/shop/{self.name}/{self.pk}'
    
  class Meta:
    db_table = 'product'  

def image_upload_path(instance, filename):
    return f'upload_file/product/{instance.product.name}/{filename}'    

class ProductImage(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  
    #제품 사진
  product_Image = models.ImageField(upload_to="upload_file/product/main", blank=True, default='')
  
  #제품 설명 사진
  information_Image = models.ImageField(upload_to="upload_file/product/information", blank=True, default='')
  
  #제품 사양 사진
  specification_Image = models.ImageField(upload_to="upload_file/product/specification", blank=True, default='')
  
  #제품 옵션 사진
  option_Image = models.ImageField(upload_to="upload_file/product/option", blank=True, default='')
      