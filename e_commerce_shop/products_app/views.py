# products_app/views.py
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from .models import Category, Product


# Create your views here.



class AllProductsListView(ListView):
    model = Product
    template_name = 'common/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(in_stock=True)


class CategoryListView(ListView):
    model = Product
    template_name = 'products/product_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=category_slug)
        queryset = Product.objects.filter(category=category)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        context['category'] = get_object_or_404(Category, slug=category_slug)
        return context