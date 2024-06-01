from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('show_orders/', views.show_orders, name='show_orders'),
    
]
