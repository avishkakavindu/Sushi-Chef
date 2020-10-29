from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from store.models import *


# checkout page
@login_required(login_url='/login')
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)