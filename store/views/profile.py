from django.db.models import Prefetch
from django.shortcuts import render
from store.models import *


# menu page
def profile(request):
    context = {}

    return render(request, 'store/profile.html', context)
