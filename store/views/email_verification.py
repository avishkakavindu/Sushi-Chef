from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from store.forms import CreateUserForm
from store.decorators import unauthenticated_user
from store.models import Customer
from store.util import Util, token_generator


@unauthenticated_user
def email_verification(request,uidb64, token):
    if request.method == 'GET':
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user, token):
                return redirect('login'+'?message'+'user already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully!')

        except Exception as e:
            messages.error(request, 'Failed to verify account!')
        return redirect('login')


