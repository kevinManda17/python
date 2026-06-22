from .cart import Cart 


# create context processor  ao our cart can work on all pages of sites 

def cart(request):
    #return the default data from our cart 
    return {'cart':Cart(request)}