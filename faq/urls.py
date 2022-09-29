from django.urls import path
from . import views

urlpatterns = [
    path('faq', views.FaqListView.as_view(), name='faq_list'),
    path('faq/<int:pk>/', views.faq_detail_view, name='faq_detail'),
]

    

