from django import template
import numpy as np

register = template.Library()

delivery = 5

@register.filter
def get_quantity(dictionary, key):
    try:
        return dictionary.get(str(key))['quantity']
    except KeyError:
        return str(1)


@register.filter
def get_cost(dictionary, key):
    try:
        quantity = float(dictionary.get(str(key))['quantity'])
        unit_price = float(dictionary.get(str(key))['unit_price'])
        return '${:.2f}'.format(quantity * unit_price)
    except KeyError:
        return '${}'.format('0')


@register.filter
def get_subtotal(dictionary):
    sum = 0
    try:
        for i in dictionary.values():
            sum += np.prod(list(map(float, i.values())))
        return '${:.2f}'.format(sum)
    except KeyError:
        return '$0.00'


@register.filter
def get_total(dictionary, coupon_discount):
    sum = 0
    delivery = 5
    try:
        for i in dictionary.values():
            sum += np.prod(list(map(float, i.values())))
        if coupon_discount:
            sum -= (sum * (coupon_discount/100))
        return '${:.2f}'.format(sum + delivery)
    except KeyError:
        return '$0.00'

@register.filter
def get_coupon_discount(dictionary, coupon_discount):
    sum = 0

    for i in dictionary.values():
        sum += np.prod(list(map(float, i.values())))
    sum += delivery
    discount = sum * (coupon_discount/100)
    return '${:.2f}'.format(discount)

