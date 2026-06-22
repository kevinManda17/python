from django.contrib import admin

from .models import *
from .models import ShippingAddress

# register model on the admin section 

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)