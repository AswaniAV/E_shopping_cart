from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('-priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    context = {
        'featured_products' : featured_products,
        'latest_products' : latest_products,
    }        
    return render(request, 'index.html', context)


def list_products(request):
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    product_list = Product.objects.order_by('-priority').all()
    product_paginator = Paginator(product_list, 3)
    product_list = product_paginator.page(page)
    context = {
        'product_list': product_list
    }
    return render(request, 'products.html', context)

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)

