from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from store.models import *
import json


# cart page
@login_required(login_url='/login')
def cart(request):
    # exception no cookie named 'cart'
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    context = {
        'data': [],
        'cart': cart,
    }

    for item in cart:
        product_detail = ProductImage.objects.select_related('product').filter(product=item[0], place='Main Product Image')
        #print(product_detail[0].product.desc)
        context['data'].append(product_detail)
    # print(context['data'][0][0].product.desc)



    return render(request, 'store/cart.html', {'context': context})
