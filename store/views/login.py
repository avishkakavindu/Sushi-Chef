from django.shortcuts import render
from store.models import *


# promo page
def login(request):
    context = {}
    return render(request, 'store/login.html', context)