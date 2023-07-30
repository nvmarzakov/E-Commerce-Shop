# store/views.py
from django.shortcuts import render
from django.views.generic import ListView

from .models import Category, Product


# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }


# def all_products(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#     }
#     return render(request, 'store/home.html', context)
class AllProductsListView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'

