from django.urls import path
from . import views


urlpatterns = [
    path('osciiloscope',views.shop_Osciiloscope),
    path('detail',views.shop_detail),
    
]

