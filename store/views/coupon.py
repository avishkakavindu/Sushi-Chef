from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_list_or_404, HttpResponse
from store.models import *
from store.decorators import allowed_user
from store.forms import UpdateCustomerForm, UpdateUserForm
from django.db.models import Prefetch


@login_required(login_url='/login')
def coupon(request):
    coupons = Coupon.objects.filter(customer=request.user.customer).prefetch_related(
        Prefetch(
            'coupon_set',
            Order.objects.all(),
            to_attr='order'
        ),
    ).order_by('-active')
    context = {
        'coupons': coupons,
    }

    return render(request, 'store/coupon.html', context)
