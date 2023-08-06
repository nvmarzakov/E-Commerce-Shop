# add session , delete session etc.
from _pydecimal import Decimal

from e_commerce_shop.products_app.models import Product


class Basket():
    """
    A base Basket class, providing some default behaviours that
    can be inherited ot overrided, as necessary.
    """

    # --> user sends a http request at the server and inside it there is lots of different
    # types of data that we want to access
    def __init__(self, request):
        # Start to build session
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket

    # To check if code work

    # open Python console:
    # from django.contrib.sessions.models import Session
    # s = Session.objects.get(pk='wcadk05a7588i9ie8648tkoy4uur5svl')
    # s.get_decoded() -->> then will see the number of session key(put some number)

    def add(self, product, quantity):
        """
        Adding and updating the users basket session data
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(quantity)}

        self.session.modified = True

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
    def __len__(self):
        """
        Get the basket data and count the quantity of items
        """
        return sum(item['qty'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
