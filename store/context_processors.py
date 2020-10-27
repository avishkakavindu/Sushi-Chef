from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import CreateUserForm


# Registration form
def include_registration_form(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for {}. Now you can sign in.'.format(user))

        else:
            messages.error(request, "Something went wrong. Account not created!")
    context = {
        'registration_form': form,
    }
    return context


# Login form
def include_login_form(request):
    form = AuthenticationForm()
    context = {
        'login_form': form,
    }
    return context
