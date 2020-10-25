from django.db.models import Prefetch
from django.shortcuts import render
from store.models import *


# index page
def home(request):
    products = Product.objects.prefetch_related(
        Prefetch(
            'productimage_set',
            ProductImage.objects.filter(place='Main Product Image'),
            to_attr='main_image'
        )
    ).order_by('?')[3:]  # random 3 record pass

    chefs = Chef.objects.all()

    # product = Product.objects.prefetch_related(Prefetch('review_set', ProductReview.objects.annotate(n=Count(
    # 'rating')),to_attr='r_count'))

    context = {
        'products': products,
        'five_star': [0, 1, 2, 3, 4],
        'chefs': chefs
    }
    return render(request, 'store/index.html', context)