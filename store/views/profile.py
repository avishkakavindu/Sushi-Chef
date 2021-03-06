from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from store.forms import UpdateCustomerForm, UpdateUserForm
from store.models import *


# menu page
@login_required(login_url='/login')
# @allowed_user(allowed_roles=['customer'])
def profile(request):
    msg = {'success': None, 'msg': None}

    password_form = PasswordChangeForm(request.user)
    user_details = User.objects.select_related("customer").get(username=request.user)
    customer_form = UpdateCustomerForm(instance=request.user.customer)
    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        customer_form = UpdateCustomerForm(request.POST, request.FILES, instance=request.user.customer)
        password_form = PasswordChangeForm(request.user, request.POST)

        if customer_form.is_valid() and user_form.is_valid():
            if request.FILES.get('profile_pic', False):
                Customer.objects.get(user=request.user).profile_pic.delete(save=True)

            user_form.save()
            customer_form.save()
            msg = {'success': True, 'msg': "Account updated!"}
            user_details = User.objects.select_related("customer").get(username=request.user)

        if password_form.data['old_password'] != '' or password_form.data['new_password1'] != '' or password_form.data['new_password2'] != '':
            if password_form.is_valid():
                user_pass = password_form.save()
                update_session_auth_hash(request, user_pass)
                msg = {'success': True, 'msg': "Password changed!"}
            else:
                msg = {'success': False, 'msg': 'Failed to change password!'}
        else:
            password_form = PasswordChangeForm(request.user)

    if msg['success']:
        messages.success(request, msg['msg'])
    elif not msg['success']:
        messages.error(request, msg['msg'])

    context = {
        'user_details': user_details,
        'customer_form': customer_form,
        'user_form': user_form,
        'password_form': password_form,
    }

    return render(request, 'registration/profile.html', context)




