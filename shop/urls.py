from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop),
    path('detail',views.shop_detail),
]