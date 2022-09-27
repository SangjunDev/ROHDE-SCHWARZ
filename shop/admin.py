from django.contrib import admin

from .models import *

class ProductImageInline(admin.TabularInline):
  model = ProductImage
  
class ProductAdmin(admin.ModelAdmin):
  inlines = [ProductImageInline, ]  

admin.site.register(Product, ProductAdmin )
