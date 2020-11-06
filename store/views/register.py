from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import *
from store.forms import CreateUserForm
from store.decorators import unauthenticated_user
from store.models import Customer
from django.contrib.auth.models import Group


# Register page
@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
            )

            messages.success(request, 'Account was created for {}. Now you can sign in.'.format(username))
            return redirect('login')

        else:
            messages.error(request, "Something went wrong. Account not created!")

    context = {
        'registration_form': form,
    }
    return render(request, 'registration/signup.html', context)

