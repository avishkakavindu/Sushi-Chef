import random
import string
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
from .models import Customer, Coupon
from .util import Util

domain = settings.DOMAIN


def generate_coupon():
    COUPON_CHARS = string.ascii_letters + string.digits
    COUPON_LENGTH = 6

    code = "".join(random.choice(COUPON_CHARS) for i in range(COUPON_LENGTH))

    return code


def send_coupon_email(username, email, domain, discount):
    link = '/my_coupons'
    schema = 'https'
    url = '{}://{}{}'.format(schema, domain, link)

    email_body = 'Congratulations! You have got {}% coupon'.format(discount)
    subject = 'You have a coupon'
    link_text = 'Shop Now'
    email_reason = "You're receiving this email because you received a coupon from {}".format(domain)

    data = {
        'receiver': email,
        'email_body': {
            'username': username,
            'email_body': email_body,
            'link': url,
            'link_text': link_text,
            'email_reason': email_reason,
            'site_name': domain
        },
        'email_subject': subject,
    }

    Util.send_email(data)


@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True and instance.is_superuser == False:
        # creating inactive user
        instance.is_active = False
    # else:
    #     print("Updating User Record!")


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created and user.is_superuser:
        customer = Customer(user=user)
        customer.save()


@receiver(post_save, sender=Customer)
def create_coupon(sender, instance, created, **kwargs):
    if created:
        discount = 10
        Coupon.objects.create(
            code=generate_coupon(),
            desc="New user Coupon 10% off from your first purchase.(Valid 10 days)",
            discount=discount,
            customer=instance.user.customer
        )

        username = instance.user.username
        email = instance.user.email

        send_coupon_email(username, email, domain, discount)


@receiver(post_save, sender=Coupon)
def notify_coupon(sender, instance, created, **kwargs):
    if created:
        discount = instance.discount
        username = instance.customer.user.username
        email = instance.customer.user.email

        send_coupon_email(username, email, domain, discount)


@receiver(user_logged_in)
def send_coupon_alert(sender, user, request, **kwargs):
    now = timezone.now()
    coupons = Coupon.objects.filter(customer=request.user.customer, valid_from__lte=now, valid_to__gte=now, active=True)

    if coupons.exists():
        messages.info(request, "You have a coupon!")
