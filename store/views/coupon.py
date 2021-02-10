from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render
from store.models import *


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
