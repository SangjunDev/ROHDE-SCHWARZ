from django.contrib import admin
from .models import Notic

# Register your models here.


class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'writer', 
        'hits',
        'registered_date',
        )
    search_fields = ('title', 'content', 'writer__user_id',)

admin.site.register(Notic, NoticeAdmin)









#class NoticAdmin(admin.ModelAdmin):
#  list_display = ('id','title', 'writer', )
  
#admin.site.register(Notic, NoticAdmin)  