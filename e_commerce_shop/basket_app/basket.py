# add session , delete session etc.


class Basket():
    """
    A base Basket class, providing some default behaviours that
    can be inherited ot overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket

    # To check if code work

    # open Python console:
    # from django.contrib.sessions.models import Session
    # s = Session.objects.get(pk='wcadk05a7588i9ie8648tkoy4uur5svl')
    # s.get_decoded() -->> then will see the number of session key
    def add(self, product):
        """
        Adding and updating the users basket session data
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price': product.price}

        self.session.modified = True