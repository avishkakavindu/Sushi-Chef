from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from store.models import *
from store.decorators import allowed_user


# checkout page
@login_required(login_url='/login')
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
