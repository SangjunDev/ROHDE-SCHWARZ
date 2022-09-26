from django.db import models

class oscillo(models.Model):
  # 상품명
  name = models.TextField()
  # 간단한 설명
  about = models.TextField()
  # 상품 이미지
  image = models.ImageField(upload_to='upload_file/shop_img/osi_img/', blank=False)
  
  def __str__(self):
    return f'{self.name}'
  
class mnc(models.Model):
  # 상품명
  name = models.TextField()
  # 간단한 설명
  about = models.TextField()
  # 상품 이미지
  image = models.ImageField(upload_to='upload_file/shop_img/mnc_img/', blank=False)
  
  def __str__(self):
    return f'{self.name}'
  
class ps(models.Model):
  # 상품명
  name = models.TextField()
  # 간단한 설명
  about = models.TextField()
  # 상품 이미지
  image = models.ImageField(upload_to='upload_file/shop_img/ps_img/', blank=False)
  
  def __str__(self):
    return f'{self.name}'

class sa(models.Model):
  # 상품명
  name = models.TextField()
  # 간단한 설명
  about = models.TextField()
  # 상품 이미지
  image = models.ImageField(upload_to='upload_file/shop_img/sa_img/', blank=False)
  
  def __str__(self):
    return f'{self.name}'
  
class sg(models.Model):
  # 상품명
  name = models.TextField()
  # 간단한 설명
  about = models.TextField()
  # 상품 이미지
  image = models.ImageField(upload_to='upload_file/shop_img/sg_img/', blank=False)
  
  def __str__(self):
    return f'{self.name}'
  
class na(models.Model):
  # 상품명
  name = models.TextField()
  # 간단한 설명
  about = models.TextField()
  # 상품 이미지
  image = models.ImageField(upload_to='upload_file/shop_img/na_img/', blank=False)
  
  def __str__(self):
    return f'{self.name}'
  
class au(models.Model):
  # 상품명
  name = models.TextField()
  # 간단한 설명
  about = models.TextField()
  # 상품 이미지
  image = models.ImageField(upload_to='upload_file/shop_img/au_img/', blank=False)
  
  def __str__(self):
    return f'{self.name}'
  
class emc(models.Model):
  # 상품명
  name = models.TextField()
  # 간단한 설명
  about = models.TextField()
  # 상품 이미지
  image = models.ImageField(upload_to='upload_file/shop_img/emc_img/', blank=False)
  
  def __str__(self):
    return f'{self.name}'              
  
class pm(models.Model):
    # 상품명
  name = models.TextField()
  # 간단한 설명
  about = models.TextField()
  # 상품 이미지
  image = models.ImageField(upload_to='upload_file/shop_img/pm_img/', blank=False)
  
  def __str__(self):
    return f'{self.name}'       
