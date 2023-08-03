# basket_app.views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from e_commerce_shop.basket_app.basket import Basket
from e_commerce_shop.products_app.models import Product


def basket_summary(request):
    return render(request, 'basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))  # -->> get product id
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)
        response = JsonResponse({
            'test': 'data',
        })

        return response
