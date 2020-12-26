from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from store.models import *
from store.decorators import allowed_user
from store.forms import DeliveryForm, CouponForm
import json
from decimal import Decimal


# checkout page
@login_required(login_url='/login')
def checkout(request):
    # direct redirecting to checkout page restrictions
    if 'HTTP_REFERER' in request.META.keys() and request:
        try:
            previous_url = request.META.get('HTTP_REFERER')
            if previous_url == 'http://127.0.0.1:8000/checkout':
                pass
            elif previous_url == 'http://127.0.0.1:8000/cart':
                if len(json.loads(request.COOKIES['cart'])) != 0:
                    pass
                else:
                    raise Http404
            else:
                raise Http404
        except:
            raise Http404

    else:
        raise Http404

    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    user_detail = Customer.objects.get(user=request.user)

    coupon_id = None
    coupon_discount = None

    user_address = {
        'address': user_detail.address,
        'city': user_detail.city,
        'state': user_detail.state,
        'zipcode': user_detail.zipcode,
    }

    delivery_form = DeliveryForm(initial=user_address)
    coupon_form = CouponForm()

    if request.method == 'POST':
        delivery_form = DeliveryForm(request.POST)
        coupon_form = CouponForm(request.POST)

        # if redeem btn clicked
        if 'coupon_btn' in request.POST:
            # fill the form with user details
            user_detail = Customer.objects.get(user=request.user)

            user_address = {
                'address': user_detail.address,
                'city': user_detail.city,
                'state': user_detail.state,
                'zipcode': user_detail.zipcode,
            }

            delivery_form = DeliveryForm(initial=user_address)

            # coupon process
            now = timezone.now()
            coupon_form = CouponForm(request.POST)

            if coupon_form.is_valid():
                code = coupon_form.cleaned_data['coupon_code']

                try:
                    coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)
                    coupon_discount = coupon.discount
                    coupon_id = coupon.id
                    request.session['coupon_id'] = coupon_id

                except Coupon.DoesNotExist:
                    request.session['coupon_id'] = None
                    messages.error(request, "Coupon code ({}) is invalid or has expired!".format(code))

        # if checkout btn clicked
        if 'checkout_btn' in request.POST:
            if delivery_form.is_valid():
                print(cart)
                total_payment = calculateTotal(cart)
                # save delivery address to Order
                delivery_details = delivery_form.save(commit=False)
                delivery_details.customer = request.user.customer

                # if coupon added
                try:
                    coupon_id = request.session['coupon_id']

                except KeyError:
                    coupon_id = None

                if coupon_id:
                    coupon = Coupon.objects.get(id=coupon_id)
                    coupon.active = False
                    coupon_discount = coupon.discount

                    total_payment -= (Decimal(total_payment) * (Decimal(coupon_discount) / 100))
                    # update order
                    delivery_details.coupon = coupon
                    delivery_details.total = total_payment
                    delivery_details.save()
                    coupon.save()
                    del request.session['coupon_id']

                else:
                    # update order
                    delivery_details.total = total_payment
                    delivery_details.save()

                # save individual ordered product and details
                for item in cart:
                    product = Product.objects.get(id=item)
                    quantity = cart[item]['quantity']
                    cost_detail = Product.objects.filter(id=item).values('price', 'discount')
                    unit_price = cost_detail[0]['price']
                    discount = cost_detail[0]['discount'] / 100
                    total_price = Decimal(quantity) * Decimal(unit_price)
                    paid = total_price - (total_price * Decimal(discount))

                    ordered_product = OrderedProduct(product=product, quantity=quantity,
                                                     offer=cost_detail[0]['discount'], paid=paid,
                                                     order=delivery_details)
                    ordered_product.save()

                messages.success(request, 'Order saved! Thank you for the purchase!')
                # cart clear
                response = redirect(request.path)
                response.delete_cookie('cart')
                return response

            # checkout process error
            messages.error(request, 'Checkout process terminated!')
            return redirect(request.path)

    context = {
        'data': [],
        'cart': cart,
        'delivery_form': delivery_form,
        'coupon_detail': [coupon_id, coupon_discount]
    }

    for item in cart:
        product_detail = Product.objects.get(id=item[0])
        # print(product_detail[0].product.desc)
        context['data'].append(product_detail)
    # print(context['data'][0][0].product.desc)

    return render(request, 'store/checkout.html', context)


def calculateTotal(cart):
    # {'2': {'unit_price': '98.00', 'quantity': 1},
    #  '3': {'unit_price': '6.00', 'quantity': 1},
    #  '6': {'unit_price': '49.50', 'quantity': 1}}
    total = 0
    for product in cart.keys():
        quantity = cart[product]['quantity']
        cost_detail = Product.objects.filter(id=product).values('price', 'discount')
        cost = cost_detail[0]['price'] * quantity
        discount = (cost_detail[0]['discount']/100) * cost

        total += (cost - discount)

    return Decimal(total)


