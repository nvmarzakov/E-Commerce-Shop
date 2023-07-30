# store urls.py
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = (
    path('', views.AllProductsListView.as_view(), name='all_products'),
    path('item/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
)
