# store urls.py
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = (
    # path('', views.all_products, name='all_products'),
    path('', views.AllProductsListView.as_view(), name='all_products'),
    path('item/<int:pk>', views.product_detail, name='product_detail')
)
