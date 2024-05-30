from django.urls import path
from . import views

urlpatterns = [
    path('show_accounts/', views.show_accounts, name='show_accounts'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart') 
]
