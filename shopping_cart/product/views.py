from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)

def products(request):    
    return render(request, 'products.html')

