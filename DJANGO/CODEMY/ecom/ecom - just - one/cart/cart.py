from store.models import  *

class Cart():
    "To show on all pages "

    def __init__(self, request ):
        self.session = request.session 

        # get the current sesion key 
        cart = self.session.get('session_key')

        # if the is new ,no session key ! create one 
        if 'session_key' not in request.session :
            cart = self.session['session_key'] = {}

        # make sure cart is available on all pages of sites 
        self.cart = cart 
        

    def add(self, product):
        product_id = str(product.id)  

        # logic 
        if product_id in self.cart :
            pass
        else :
            self.cart[product_id] = {'price':str( product.price )}      
            self.session.modified = True 