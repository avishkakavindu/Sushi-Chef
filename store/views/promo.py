from django.db.models import Prefetch
from django.shortcuts import render
from store.models import *


# promo page
def promo(request):
    promos = Product.objects.exclude(discount='0').prefetch_related(
        Prefetch(
            'productimage_set',
            ProductImage.objects.filter(place='Main Product Image'),
            to_attr='main_image'
        )
    )
    context = {
        'promos': promos
    }
    return render(request, 'store/promo.html', context)