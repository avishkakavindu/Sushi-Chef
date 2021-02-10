from django.db.models import Prefetch
from django.shortcuts import render
from store.models import Product, Wishlist, ProductImage


# menu page
def menu(request):
    products = Product.objects.order_by('name').prefetch_related(
        Prefetch(
            'productimage_set',
            ProductImage.objects.filter(place='Main Product Image'),
            to_attr='main_image'
        ),
    )
    try:
        wishes = Wishlist.objects.filter(customer=request.user.customer).values_list('product', flat=True)
    except AttributeError:
        wishes = []

    context = {
        # 'products': products,
        'five_star': [0, 1, 2, 3, 4],
        'wishes': wishes,
    }

    return render(request, 'store/menu.html', context)
