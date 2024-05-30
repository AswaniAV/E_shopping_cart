from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from product.models import Product
from customer.models import Customer

# Create your views here.

def cart (request):
    return render(request, 'cart.html')

@login_required
def add_to_cart(request, pk):
    if request.method == 'POST':
        user = request.user

        try:
            customer = user.customer
        except Customer.DoesNotExist:
            messages.error(request, 'Please create your profile first.')
            return redirect('show_accounts')

        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, pk=pk)

        cart_order, created = Order.objects.get_or_create(owner=customer, order_status=Order.CART_STAGE)
        order_item, created = OrderItem.objects.get_or_create(product = product, owner=cart_order)

        if created:
            order_item.quantity = quantity
        else:
            order_item.quantity += quantity

        order_item.save()
        messages.success(request, 'Product added to cart successfully.')

    return redirect('cart')
