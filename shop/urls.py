from django.urls import path
from . import views


urlpatterns = [
    path('<str:name>/<int:pk>/', views.ShopDetail.as_view()),
    path('',views.ShopList.as_view()),
    #path('',views.shop_index),
    #path('detail',views.shop_detail),
    
]

