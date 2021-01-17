from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group, User
from store.forms import CreateUserForm
from store.decorators import unauthenticated_user
from store.models import Customer
from store.util import Util, token_generator
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


# Register page
@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        try:
            print(request.POST)
            user = User.objects.get(email=request.POST['email'])

            if user.is_active:
                messages.success(request, 'You already have an account!')

            else:
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = token_generator.make_token(user)

                domain = get_current_site(request).domain
                link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
                url = 'http://{}{}'.format(domain, link)

                email_body = "Hi {},\nPlease use following url to verify your email\n {}\n\n Thanks for using our " \
                             "site!\nThe {} team".format(user.username, url, domain)

                data = {
                    'receiver': user.email,
                    'email_body': email_body,
                    'email_subject': 'Verify your Email',
                }

                Util.send_email(data)

                messages.success(
                    request,
                    'Verification email was sent. Please verify your email.'
                )
            return redirect('login')
        except ObjectDoesNotExist:
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='customer')
                user.groups.add(group)
                Customer.objects.create(
                    user=user,
                )

                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = token_generator.make_token(user)

                domain = get_current_site(request).domain
                link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
                url = 'http://{}{}'.format(domain, link)

                email_body = "Hi {},\nPlease use following url to verify your email\n {}\n\n Thanks for using our " \
                             "site!\nThe {} team".format(username, url, domain)

                data = {
                    'receiver': user.email,
                    'email_body': email_body,
                    'email_subject': 'Verify your Email',
                }

                Util.send_email(data)

                messages.success(
                    request,
                    'Account was created for {} and verification email was sent. Please verify your email.'.format(username)
                )
                return redirect('login')

            else:
                messages.error(request, "Something went wrong. Account not created!")

    context = {
        'registration_form': form,
    }
    return render(request, 'registration/signup.html', context)
