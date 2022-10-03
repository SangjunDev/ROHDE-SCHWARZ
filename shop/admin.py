from django.contrib import admin

from .models import *

class ProductImageInline(admin.TabularInline):
  model = ProductImage
  
class InfoImageInline(admin.TabularInline):
  
  model = InfoImage

class SpecImageInline(admin.TabularInline):
  model = SpecImage
  
class OptionImageInline(admin.TabularInline):
  model = OptionImage
  
class ProductAdmin(admin.ModelAdmin):
  inlines = [ProductImageInline, InfoImageInline, SpecImageInline,  OptionImageInline ]
  
  class Meta:
    model = Product  

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}   
  
admin.site.register(Category, CategoryAdmin) 
