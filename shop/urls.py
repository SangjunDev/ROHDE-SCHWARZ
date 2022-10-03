from django.urls import path
from . import views


urlpatterns = [
    path('',views.ShopList.as_view(), name='shop_list'),
    path('<str:category>/<str:name>/<int:pk>/', views.ShopDetail, name='shop_detail'),
    
]

