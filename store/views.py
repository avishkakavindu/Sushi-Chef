from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *


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


# menu page
def menu(request):
    products = Product.objects.prefetch_related(
        Prefetch(
            'productimage_set',
            ProductImage.objects.filter(place='Main Product Image'),
            to_attr='main_image'
        )
    )

    context = {
        'products': products,
        'five_star': [0, 1, 2, 3, 4]
    }

    return render(request, 'store/menu.html', context)


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


# cart page
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


# checkout page
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


# product detail page
def product_detail(request, product_id):
    product_detail = get_list_or_404(ProductReview.objects.all().select_related('product', 'customer'), product=product_id)
    images = get_object_or_404(Product, pk=product_id)

    context = {
        'product_details': product_detail,
        'main_img': images.productimage_set.filter(place="Main Product Image").all(),
        'sub_img1': images.productimage_set.filter(place="Sub Image 1").all(),
        'sub_img2': images.productimage_set.filter(place="Sub Image 2").all(),
        'five_star': [0, 1, 2, 3, 4],
    }
    return render(request, 'store/product.html', context)
