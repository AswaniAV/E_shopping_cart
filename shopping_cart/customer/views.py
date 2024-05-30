from django.shortcuts import render, redirect, get_object_or_404
from customer.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from product.models import Product
from order.models import Order, OrderItem

def show_accounts(request):
    context = {}

    if request.method == 'POST' and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            address = request.POST.get('address')

            if User.objects.filter(username=username).exists():
                raise ValueError("Username already exists")
            if User.objects.filter(email=email).exists():
                raise ValueError("Email already exists")

            user = User.objects.create_user(username=username, email=email, password=password)
            customer = Customer.objects.create(name=username, user=user, phone=phone, address=address, email=email)
            success_message = "Registration successful. You can now log in."
            messages.success(request, success_message)

        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, "An error occurred during registration")

    if 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials, please try again.')

    return render(request, 'account.html', context)

def logout(request):
    auth_logout(request)
    messages.info(request, 'Logout successfully')
    return redirect('show_accounts')


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

@login_required
def cart(request):
    user = request.user

    try:
        customer = user.customer
    except AttributeError:
        messages.error(request, 'Please create your profile first')    
        return redirect('show_accounts')

    cart_order, created = Order.objects.get_or_create(owner=customer, order_status=Order.CART_STAGE)
    cart_items = cart_order.added_items.all()
    subtotal = sum(item.price for item in cart_items)
    shipping_fee = 50
    total_price = subtotal + shipping_fee

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping_fee': shipping_fee,
        'total_price': total_price,
    }

    return render(request, 'cart.html', context)

@login_required
def remove_from_cart(request, item_id):
    ordered_item = get_object_or_404(OrderItem, id=item_id)
    ordered_item.delete()
    messages.success(request, 'Product removed from cart successfully.')
    return redirect('cart')