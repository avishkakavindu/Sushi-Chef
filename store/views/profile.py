from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from store.models import *
from store.decorators import allowed_user
from store.forms import UpdateCustomerForm, UpdateUserForm


# menu page
@login_required(login_url='/login')
# @allowed_user(allowed_roles=['customer'])
def profile(request):
    user_details = User.objects.select_related("customer").get(username=request.user)
    customer_form = UpdateCustomerForm(instance=request.user.customer)
    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        customer_form = UpdateCustomerForm(request.POST, request.FILES, instance=request.user.customer)
        if customer_form.is_valid() and user_form.is_valid():
            user_form.save()
            customer_form.save()

    context = {
        'user_details': user_details,
        'customer_form': customer_form,
        'user_form': user_form
    }

    return render(request, 'registration/profile.html', context)




