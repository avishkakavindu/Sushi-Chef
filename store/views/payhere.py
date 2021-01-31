from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_list_or_404, HttpResponse
from store.models import *
from store.decorators import allowed_user
from store.forms import UpdateCustomerForm, UpdateUserForm
from django.db.models import Prefetch


def payhere(request):
    pass