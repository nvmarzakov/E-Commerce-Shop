# products_app urls.py
from django.urls import path
from . import views

app_name = 'products_app'

urlpatterns = (
    path('', views.AllProductsListView.as_view(), name='all_products'),
    path('item/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('search/<slug:category_slug>/', views.CategoryListView.as_view(), name='category_list')
)
