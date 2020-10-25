from django.shortcuts import render
from store.models import *


# cart page
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)
