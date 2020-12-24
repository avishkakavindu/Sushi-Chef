from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from store.models import *
from store.decorators import allowed_user
from store.forms import UpdateCustomerForm, UpdateUserForm


@login_required(login_url='/login')
def order_history(request):
    context = {}

    return render(request, 'store/order_history.html', context)
