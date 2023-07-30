# products_app/views.py

from django.views.generic import ListView, DetailView

from .models import Category, Product


# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }


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
