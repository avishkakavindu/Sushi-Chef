from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_list_or_404
from store.models import *
from store.decorators import allowed_user
from store.forms import UpdateCustomerForm, UpdateUserForm
from django.db.models import Prefetch


def get_total(items, coupon):
    pass

@login_required(login_url='/login')
def order(request, order_id):
    # get particular order with ordered items, and discounts
    order = get_list_or_404(Order.objects.filter(customer=request.user.customer).prefetch_related(
        Prefetch(
            'orderedproduct_set',
            OrderedProduct.objects.all(),
            to_attr='ordered_products'
        ),
        Prefetch('coupon', to_attr='coupon_discount')
    ),  id=order_id)

    context = {
        'orders': order,
    }

    return render(request, 'store/order.html', context)

