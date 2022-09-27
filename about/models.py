from django.db import models

# Create your models here.

class About_Post(models.Model):
  name = models.CharField(max_length=50)
  content = models.TextField()
  
  
  # 게시글의 제목(postname)이 Post object 대신하기
  def __str__(self):
    return self.postname


class history_post(models.Model):
  name = models.CharField(max_length=50)
  cotent = models.TextField()



  def __str__(self):
    return self.name
