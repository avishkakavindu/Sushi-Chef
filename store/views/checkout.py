from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import *
from store.decorators import allowed_user
from store.forms import DeliveryForm
import json


# checkout page
@login_required(login_url='/login')
def checkout(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    user_detail = Customer.objects.get(user=request.user)

    user_address = {
        'address': user_detail.address,
        'city': user_detail.city,
        'state': user_detail.state,
        'zipcode': user_detail.zipcode,
    }

    delivery_form = DeliveryForm(initial=user_address)

    if request.method == 'POST':
        delivery_form = DeliveryForm(request.POST)
        if delivery_form.is_valid():
            # save delivery address to Order
            delivery_details = delivery_form.save(commit=False)
            delivery_details.customer = request.user.customer
            delivery_details.save()
            # save individual ordered product and details
            for item in cart:
                product = Product.objects.get(id=item)
                quantity = cart[item]['quantity']
                cost_detail = Product.objects.filter(id=item).values('price', 'discount')
                unit_price = cost_detail[0]['price']
                discount = cost_detail[0]['discount'] / 100
                paid = quantity * unit_price - (unit_price * discount)
                ordered_product = OrderedProduct(product=product, quantity=quantity, paid=paid, order=delivery_details)
                ordered_product.save()

                messages.success(request, 'Order saved! Thank you for the purchase!')

            return redirect(request.path)

    context = {
        'data': [],
        'cart': cart,
        'delivery_form': delivery_form,
    }
    for item in cart:
        product_detail = ProductImage.objects.select_related('product').filter(product=item[0], place='Main Product Image')
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

    return '{:.2f}'.format(total)


