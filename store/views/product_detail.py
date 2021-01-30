from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib import messages
from django.db.models import Prefetch
from store.models import Product, ProductReview
from store.forms import ProductReviewForm


# product detail page
def product_detail(request, product_id):
    form = ProductReviewForm()

    product_details = Product.objects.filter(pk=product_id).prefetch_related(
        Prefetch(
            'productreview_set',
            ProductReview.objects.all(),
            to_attr='reviews'
        )
    )

    images = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = Product.objects.get(pk=product_id)
            review.customer = request.user.customer
            review.save()

            messages.success(request, 'Review saved! Thank you for the review!')
            return redirect(request.path)

        else:
            messages.error(request, "Something went wrong. Review not recorded!")


    context = {
        'product_details': product_details,
        'main_img': images.productimage_set.filter(place="Main Product Image").all(),
        'sub_img1': images.productimage_set.filter(place="Sub Image 1").all(),
        'sub_img2': images.productimage_set.filter(place="Sub Image 2").all(),
        'five_star': [0, 1, 2, 3, 4],
        'review_form': form
    }
    return render(request, 'store/product.html', context)
