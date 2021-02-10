from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    context = {
        'error': False
    }
    if request.method == 'POST':
        username_or_email = request.POST['username']

        try:
            # get username by email
            username = User.objects.get(email=username_or_email).username
        except User.DoesNotExist:
            username = request.POST['username']

        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, "Login successfull")
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials, Please check username/email or password.')
            context['error'] = True

    return render(request, "registration/login.html", context=context)