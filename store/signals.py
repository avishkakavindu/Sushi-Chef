import random, string
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib import messages
from django.dispatch import receiver
from django.utils import timezone
from .models import Customer, Coupon


def generate_coupon():
    COUPON_CHARS = string.ascii_letters + string.digits
    COUPON_LENGTH = 6

    code = "".join(random.choice(COUPON_CHARS) for i in range(COUPON_LENGTH))

    return code


@receiver(post_save, sender=Customer)
def create_coupon(sender, instance, created, **kwargs):
    if created:
        Coupon.objects.create(
            code=generate_coupon(),
            desc="New user Coupon 10% off from your first purchase.(Valid 10 days)",
            discount=10,
            customer=instance.user.customer
        )


@receiver(user_logged_in)
def send_coupon_alert(sender, user, request, **kwargs):
    now = timezone.now()
    coupons = Coupon.objects.filter(customer=request.user.customer, valid_from__lte=now, valid_to__gte=now, active=True)

    if coupons.exists():
        messages.info(request, "You have a coupon!")


