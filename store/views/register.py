from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from store.decorators import unauthenticated_user
from store.forms import CreateUserForm
from store.models import Customer
from store.util import Util, token_generator


# Register page
@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        domain = get_current_site(request).domain
        schema = request.is_secure() and "https" or "http"

        data = {
            'receiver': '',
            'email_body': {
                            'username': '',
                            'email_body': '',
                            'link': '',
                            'link_text': 'Verify Your Email',
                            'email_reason': "You're receiving this email because you signed up in {}".format(domain),
                            'site_name': domain
                        },
            'email_subject': 'Verify your Email',
        }

        try:
            user = User.objects.get(email=request.POST['email'])

            if user.is_active:
                messages.success(request, 'You already have an account!')

            else:
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = token_generator.make_token(user)

                link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
                url = '{}://{}{}'.format(schema, domain, link)

                email_body = 'Verify your email to finish signing up for Sushi Chef'

                data['receiver'] = user.email
                data['email_body']['username'] = user.username
                data['email_body']['email_body'] = email_body
                data['email_body']['link'] = url

                Util.send_email(data)

                messages.success(
                    request,
                    'Verification email was sent. Please verify your email.'
                )

                context = {
                    'email': user.email
                }
                return render(request, 'store/email_verification.html', context)
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

                link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
                url = '{}://{}{}'.format(schema, domain, link)

                email_body = 'Verify your email to finish signing up for Sushi Chef'

                data['receiver'] = user.email
                data['email_body']['username'] = user.username
                data['email_body']['email_body'] = email_body
                data['email_body']['link'] = url

                Util.send_email(data)

                messages.success(
                    request,
                    'Account was created for {} and verification email was sent. Please verify your email.'.format(username)
                )

                context = {
                    'email': user.email
                }

                return render(request, 'store/email_verification.html', context)

            else:
                messages.error(request, "Something went wrong. Account not created!")

    context = {
        'registration_form': form,
    }
    return render(request, 'registration/signup.html', context)
