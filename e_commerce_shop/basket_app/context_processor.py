# basket_app>context_processor.py
from e_commerce_shop.basket_app.basket import Basket


def basket(request):
    return {'basket': Basket(request)}