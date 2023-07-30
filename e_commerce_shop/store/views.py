# store/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, Product


# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }


class AllProductsListView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/products/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(in_stock=True)
