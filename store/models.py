from django.db import models
from django.db.models import Avg, F
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


# Product related
class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.name

    # returns average ratings of the product
    @property
    def get_avg_rating(self):
        ratings = ProductReview.objects.filter(product=self).aggregate(rating_avg=Avg('rating'))
        if ratings['rating_avg'] is None:
            return 0
        else:
            return int(ratings['rating_avg'])

    # returns sale price (= Store price - discount)
    @property
    def get_sale_price(self):
        sale_price = Product.objects.filter(name=self).annotate(s_price=(
                F('price') - (F('price') * F('discount') * 100)))
        return sale_price


class ProductImage(models.Model):
    PLACEHOLDER = (
        ('Main Product Image', 'Main Product Image'),
        ('Sub Image 1', 'Sub Image 1'),
        ('Sub Image 2', 'Sub Image 2'),
    )
    product = models.ForeignKey(Product, related_name='image_set', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    place = models.CharField(max_length=20, choices=PLACEHOLDER)

    def __str__(self):
        return str(self.id)


class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='review_set', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.DecimalField(max_digits=1, decimal_places=0, default=0)

    def __str__(self):
        return str(self.id)


# -- End of Product related --

class Chef(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return str(self.id)


class Payment(models.Model):
    PAYMENT_METHOD = (
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Paypal', 'Paypal'),
    )

    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class ChefReview(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=1, decimal_places=0)

    def __str__(self):
        return str(self.id)
