from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render
from store.models import *


def get_total(items, coupon):
    pass


@login_required(login_url='/login')
def order_history(request):
    # get orders with ordered items, and discounts
    order = Order.objects.filter(customer=request.user.customer).prefetch_related(
        Prefetch(
            'orderedproduct_set',
            OrderedProduct.objects.all(),
            to_attr='ordered_products'
        ),
        Prefetch('coupon', to_attr='coupon_discount')
    ).order_by('-id')

    context = {
        'orders': order,
    }

    return render(request, 'store/order_history.html', context)

