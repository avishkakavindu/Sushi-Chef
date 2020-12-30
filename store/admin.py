from django.contrib import admin
from .models import *


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Chef)
admin.site.register(Order)
admin.site.register(OrderedProduct)
admin.site.register(Payment)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(ChefReview)
admin.site.register(Coupon)
admin.site.register(Wishlist)
