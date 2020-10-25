from django.shortcuts import render, get_object_or_404, get_list_or_404
from store.models import *


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
