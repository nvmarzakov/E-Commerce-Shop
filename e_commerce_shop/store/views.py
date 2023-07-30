# store/views.py
from django.shortcuts import render

from .models import Category, Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store/home.html', context)
