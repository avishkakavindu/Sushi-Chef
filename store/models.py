from django.db import models
from django.db.models import Avg, F
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to='images/user', default="images/user/default.jpg")
    date_created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.user)


# Product related models
class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # returns number of ratings
    @property
    def get_rating_count(self):
        return ProductReview.objects.filter(product=self).count()

    # returns average ratings of the product
    @property
    def get_avg_rating(self):
        ratings = ProductReview.objects.filter(product=self).aggregate(rating_avg=Avg('rating'))
        if ratings['rating_avg'] is None:
            return 0
        else:
            return [ratings['rating_avg'], int(ratings['rating_avg'])]

    # returns sale price (= Store price - discount)
    @property
    def get_sale_price(self):
        sale_price = Product.objects.filter(name=self).annotate(s_price=(F('price') * (100 - F('discount')) / 100))
        return sale_price[0].s_price

    # returns rating breakdown as percentage
    @property
    def get_rating_breakdown(self):
        all_obj = ProductReview.objects.filter(product=self)
        rating_count = self.get_rating_count
        try:
            breakdown = {
                'one_star': all_obj.filter(rating=1).count() / rating_count * 100,
                'two_star': all_obj.filter(rating=2).count() / rating_count * 100,
                'three_star': all_obj.filter(rating=3).count() / rating_count * 100,
                'four_star': all_obj.filter(rating=4).count() / rating_count * 100,
                'five_star': all_obj.filter(rating=5).count() / rating_count * 100,
            }
        except ZeroDivisionError:
            breakdown = {
                'one_star': 0,
                'two_star': 0,
                'three_star': 0,
                'four_star': 0,
                'five_star': 0,
            }
        return breakdown

    # get reviews
    def get_reviews(self):
        all_reviews = ProductReview.objects.filter(product=self)

        return all_reviews


class ProductImage(models.Model):
    PLACEHOLDER = (
        ('Main Product Image', 'Main Product Image'),
        ('Sub Image 1', 'Sub Image 1'),
        ('Sub Image 2', 'Sub Image 2'),
    )
    product = models.ForeignKey(Product, related_name='productimage_set', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/product')
    place = models.CharField(max_length=20, choices=PLACEHOLDER)

    def __str__(self):
        return str('{}-{}'.format(self.product, self.id))


class ProductReview(models.Model):
    customer = models.ForeignKey(Customer, related_name='productreview_set', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='productreview_set', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.DecimalField(max_digits=1, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Ratings of: ' + str(self.product)


# -- End of Product related --

# Chef related models
class Chef(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    # returns average ratings of the product
    @property
    def get_avg_rating(self):
        ratings = ChefReview.objects.filter(chef=self).aggregate(rating_avg=Avg('rating'))
        if ratings['rating_avg'] is None:
            return 0
        else:
            return int(ratings['rating_avg'])


class ChefReview(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET('Anonumous User'), related_name='chefreview_set')
    chef = models.ForeignKey(Chef, related_name='chefreview_set', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.DecimalField(max_digits=1, decimal_places=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


# -- End of Chef related *--

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    desc = models.TextField()
    valid_from = models.DateTimeField(auto_now_add=True)
    valid_to = models.DateTimeField(default=datetime.now()+timedelta(days=10))
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='coupon_set')

    def __str__(self):
        return '{} - {}'.format(self.customer, self.code)


class Order(models.Model):
    PAYMENT_METHOD = (
        ('payhere', 'Payhere'),
        ('cashondelivery', 'Cash on delivery'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    delivery = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    coupon = models.ForeignKey(Coupon, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='coupon_set')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)

    def __str__(self):
        return str(self.id)


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderedproduct_set')
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(max_digits=2, decimal_places=0)
    offer = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    paid = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id)


class PayherePaymentDetail(models.Model):
    merchant_id = models.CharField(max_length=20)
    payhere_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payhere_currency = models.CharField(max_length=3)
    method = models.CharField(max_length=10)
    card_holder_name = models.CharField(max_length=255)
    card_no = models.CharField(max_length=20)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payherepayment_set')

    def __str__(self):
        return 'order: {}-id: {}'.format(self.order_id, self.id)


class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productwishlist_set')

    def __str__(self):
        return '{}-{}'.format(self.id, self.customer)


