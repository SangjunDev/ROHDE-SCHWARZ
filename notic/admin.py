from django.contrib import admin
from .models import Notic, Document, NoticImage

# Register your models here.


class DocumentInline(admin.TabularInline):
    model = Document

class NoticImageInline(admin.TabularInline):
    model = NoticImage

class NoticAdmin(admin.ModelAdmin):
    
    inlines = [DocumentInline, NoticImageInline]
    list_display = (
        'title', 
        'writer', 
        'hits',
        'registered_date',
        )
    search_fields = ('title', 'content', 'writer__user_id',)
    
    class Meta:
        model = Notic

admin.site.register(Notic, NoticAdmin)
