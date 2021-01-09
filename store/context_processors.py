from django.db.models import Prefetch
from django.shortcuts import render
from store.filters import ProductFilter
from store.models import Product, ProductImage, Wishlist


def include_search_bar(request):
    queryset = Product.objects.order_by('name').prefetch_related(
        Prefetch(
            'productimage_set',
            ProductImage.objects.filter(place='Main Product Image'),
            to_attr='main_image'
        ),
    )
    product_filter = ProductFilter(request.GET, queryset=queryset)
    products = product_filter.qs

    context = {
        'product_filter': product_filter,
        'products': products,
    }

    return context





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
