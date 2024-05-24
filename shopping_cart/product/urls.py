from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_products/', views.list_products, name='list_products'),
]

