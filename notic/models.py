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

    
