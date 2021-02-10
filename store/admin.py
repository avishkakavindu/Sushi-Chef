from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'discount']
    search_fields = ['id', 'name']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'place', 'image']
    search_fields = ['product__name', 'place']


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'review', 'rating']
    search_fields = ['id', 'customer__user__username']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['user__username']


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'customer', 'active', 'discount']
    search_fields = ['code', 'customer__user__username']


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc']
    search_fields = ['name']


@admin.register(ChefReview)
class ChefReviewAdmin(admin.ModelAdmin):
    list_display = ['chef', 'customer', 'review', 'rating', 'date']
    search_fields = ['customer__user__username', 'chef__name']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'feedback']


@admin.register(OrderedProduct)
class OrderedProductAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product', 'offer', 'paid']
    search_fields = ['product__name', 'order__id', 'order__customer__user__username']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'telephone_no', 'payment_method', 'total']
    search_fields = ['customer__user__username', 'telephone_no']


@admin.register(PayherePaymentDetail)
class PayherePaymentDetailAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'card_holder_name']
    search_fields = ['order_id__id']

