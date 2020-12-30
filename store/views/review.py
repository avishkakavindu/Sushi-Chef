from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_list_or_404, HttpResponse
from store.models import *
from store.decorators import allowed_user
from store.forms import UpdateCustomerForm, UpdateUserForm
from django.db.models import Prefetch


@login_required(login_url='/login')
def review(request):
    dish_reviews = ProductReview.objects.filter(customer=request.user.customer).order_by('product').prefetch_related(
        Prefetch(
            'product',
            queryset=Product.objects.prefetch_related(
                Prefetch(
                    'productimage_set',
                    ProductImage.objects.filter(place='Main Product Image'),
                    to_attr='main_image'
                ),
            ),
            to_attr='reviewed_dish'
        ),
    )
    chef_reviews = ChefReview.objects.filter(customer=request.user.customer).order_by('chef').prefetch_related(
        Prefetch(
            'chef',
            queryset=Chef.objects.all(),
            to_attr='reviewed_chef'
        ),
    )

    context = {
        'dish_reviews': dish_reviews,
        'chef_reviews': chef_reviews,
        'five_star': [0, 1, 2, 3, 4],
    }

    return render(request, 'store/review.html', context)
