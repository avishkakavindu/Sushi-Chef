from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_list_or_404, HttpResponse
from store.models import *
from store.decorators import allowed_user
from store.forms import UpdateCustomerForm, UpdateUserForm
from django.db.models import Prefetch


@login_required(login_url='/login')
def wishlist(request):
    wishes = Wishlist.objects.filter(customer=request.user.customer).order_by('product').prefetch_related(
        Prefetch(
            'product',
            queryset=Product.objects.prefetch_related(
                Prefetch(
                    'productimage_set',
                    ProductImage.objects.filter(place='Main Product Image'),
                    to_attr='main_image'
                ),
            ),
            to_attr='wished_dish'
        ),
    )

    # delete wished dish
    if request.method == 'POST':
        dish_to_delete = request.POST['delete_items']
        Wishlist.objects.filter(
            customer=request.user.customer,
            product=dish_to_delete
        ).delete()

        messages.success(request, "Review deleted!")

    if request.method == 'GET':
        try:
            dish_id = request.GET['dish_id']

            dish = Product.objects.get(id=dish_id)

            wish, created = Wishlist.objects.get_or_create(
                customer=request.user.customer,
                product=dish
            )

            if created:
                return HttpResponse('Dish <b>{}</b> Added to wish list!'.format(dish.name))
            else:
                return HttpResponse('Dish <b>{}</b> is already in your wish list!'.format(dish.name))
        except:
            pass

    context = {
        'wishes': wishes,
    }

    return render(request, 'store/wishlist.html', context)
