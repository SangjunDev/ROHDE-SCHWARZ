from django.db import models

class producet(models.Model):
  # 상품명
  name = models.TextField()
  # 간단한 설명
  about = models.TextField()
  # 상품 이미지
  image = models.ImageField(upload_to='static/shop_img/img/', blank=False)
  
  def __str__(self):
    return f'{self.name}'
  
