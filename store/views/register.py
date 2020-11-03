from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import *
from store.forms import CreateUserForm
from store.decorators import unauthenticated_user


# promo page
@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for {}. Now you can sign in.'.format(user))
            return redirect('login')

        else:
            messages.error(request, "Something went wrong. Account not created!")

    context = {
        'registration_form': form,
    }
    return render(request, 'registration/signup.html', context)

