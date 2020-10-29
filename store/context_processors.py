# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import authenticate
# from django.shortcuts import render
# from django.contrib import messages
# from .forms import CreateUserForm
#
#
# # Registration form
# def include_registration_form(request):
#     form = CreateUserForm()
#
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for {}. Now you can sign in.'.format(user))
#
#         else:
#             messages.error(request, "Something went wrong. Account not created!")
#     context = {
#         'registration_form': form,
#     }
#     return render(context)
#
#
# # Login form
# def include_login_form(request):
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#
#     context = {
#         'login_form': form,
#     }
#     return context
