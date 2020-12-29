from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_list_or_404
from store.models import *
from store.decorators import allowed_user
from store.forms import UpdateCustomerForm, UpdateUserForm
from django.db.models import Prefetch


@login_required(login_url='/login')
def wishlist(request):

    wishes = Wishlist.objects.filter(customer=request.user.customer).prefetch_related(
        Prefetch('product',
                 queryset=Product.objects.prefetch_related(
                     Prefetch(
                         'productimage_set',
                         ProductImage.objects.filter(place='Main Product Image'),
                         to_attr='main_image'
                        ),
                 ),
                 to_attr='wished_img'
        ),
        Prefetch(
            'product',
            to_attr='wished_dish'
        )
    )

    context = {
        'wishes': wishes,
    }

    return render(request, 'store/wishlist.html', context)

