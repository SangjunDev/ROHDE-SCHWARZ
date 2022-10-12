from django.urls import path
from . import views

urlpatterns = [
    path('notic', views.NoticListView.as_view(), name='notic_list'),
    path('notic/<int:pk>/', views.notic_detail_view, name='notic_detail'),

 
]

    

