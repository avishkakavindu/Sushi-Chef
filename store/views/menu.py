from django.db.models import Prefetch
from django.shortcuts import render
from store.models import *


# menu page
def menu(request):
    products = Product.objects.prefetch_related(
        Prefetch(
            'productimage_set',
            ProductImage.objects.filter(place='Main Product Image'),
            to_attr='main_image'
        ),
    )

    context = {
        'products': products,
        'five_star': [0, 1, 2, 3, 4]
    }

    return render(request, 'store/menu.html', context)
