from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from store.models import *
from store.decorators import allowed_user


# menu page
@login_required(login_url='/login')
# @allowed_user(allowed_roles=['customer'])
def profile(request, user_name):
    user_details = get_object_or_404(Customer.objects.all(), user=user_name)

    context = {
        'user_details': user_details
    }

    return render(request, 'registration/profile.html', context)
