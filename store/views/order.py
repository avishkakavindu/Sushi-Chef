from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_list_or_404
from store.models import *
from store.decorators import allowed_user
from store.forms import UpdateCustomerForm, UpdateUserForm
from django.db.models import Prefetch
from decimal import Decimal


def get_order_summary(items, coupon_discount, delivery):
    """ Calculates the sub total """
    sub_total = sum([item.paid for item in items])
    coupon_discount = sub_total * (Decimal(coupon_discount) / 100)
    context = {
        'subtotal': sub_total,
        'total': sub_total - coupon_discount + delivery,
        'coupon_discount': coupon_discount
    }
    return context


@login_required(login_url='/login')
def order(request, order_id):
    # get particular order with ordered items, and discounts
    order_detail = get_list_or_404(Order.objects.filter(customer=request.user.customer).prefetch_related(
        Prefetch(
            'orderedproduct_set',
            OrderedProduct.objects.all().prefetch_related(  # prefetch the product details from product model
                Prefetch(
                    'product',
                    to_attr='the_product',
                )
            ),
            to_attr='ordered_products'
        ),
        Prefetch('coupon', to_attr='coupon_discount'),

    ),  id=order_id)
    payment_detail = PayherePaymentDetail.objects.get(order_id=order_id)

    # ordered items details
    items = order_detail[0].ordered_products
    delivery = order_detail[0].delivery
    # is coupon discount added?
    try:
        coupon_discount = order_detail[0].coupon_discount.discount
    except AttributeError:
        coupon_discount = 0

    context = {
        'order_detail': order_detail,
        'payment_detail': payment_detail,
        # calculate sub total and total
        'order_summary': get_order_summary(items, coupon_discount, delivery),
    }

    return render(request, 'store/order.html', context)

