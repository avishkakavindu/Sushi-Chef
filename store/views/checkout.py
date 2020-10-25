from django.shortcuts import render
from store.models import *


# checkout page
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)