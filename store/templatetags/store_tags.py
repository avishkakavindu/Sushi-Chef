from django import template
from django.utils import timezone
from django.utils.safestring import mark_safe
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

    try:
        for i in dictionary.values():
            sum += np.prod(list(map(float, i.values())))
        if coupon_discount:
            sum -= (sum * (coupon_discount / 100))
        return '${:.2f}'.format(sum + delivery)
    except KeyError:
        return '$0.00'


@register.filter
def get_coupon_discount(dictionary, coupon_discount):
    sum = 0

    for i in dictionary.values():
        sum += np.prod(list(map(float, i.values())))
    sum += delivery
    discount = sum * (coupon_discount / 100)
    return '${:.2f}'.format(discount)


def check_coupon_status(valid_to, order):
    now = timezone.now()

    if now > valid_to or not(not order):
        return False  # expired
    return True  # active


@register.filter
def is_active(valid_to, order):
    if check_coupon_status(valid_to, order):
        return True  # active
    return False  # expired


@register.filter
def coupon_status(valid_to, order):
    if check_coupon_status(valid_to, order):
        return mark_safe("<span style='color: #70bf2b'>Available!</span>")
    else:
        if not order:
            return mark_safe("<span style='color: #dd4646'>Expired!</span>")
        return mark_safe("<a href='order/{}'>#{}</a>".format(order[0], order[0]))

