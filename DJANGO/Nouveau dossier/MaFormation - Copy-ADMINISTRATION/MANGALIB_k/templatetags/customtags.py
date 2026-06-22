from django import template 
from django.template.defaultfilters import stringfilter


# register1=template.Library()

# @register1.filter(name='other')
# @stringfilter
# def custom(value):
#     return value[0]

# @register1.filter(name="lengthis")
# def checkname(value, size ):
#     return len(value) == size 

register=template.Library()

@register.simple_tag(name='hi')
def hello(username):
    return f"Hello Kevin Manda {username}"