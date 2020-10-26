from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Registration form
def include_registration_form(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

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
