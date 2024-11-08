from django import template
from ..VARIABLES import search

'''
create a custom HTML filter to use it
in user cart page for make total prices
'''

register = template.Library()


#---------------$ normal filter $---------------#
@register.filter
def totalMath(price, quantity):
    return price * quantity


#---------------$ filter using requset $---------------#
@register.simple_tag(takes_context=True)
def base_items_count(context):
    items_count = 0
    request = context['request']
    if request.user.is_authenticated:
        user = request.user.id
        user_cart = search('Cart',user=user)[0]
        user_items = search('CartItems',cart=user_cart)
        items_count = user_items.count() if user_items else 0
    return items_count