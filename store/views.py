from django.shortcuts import render


# index page
def home(request):
    context = {}
    return render(request, 'store/index.html', context)


# menu page
def menu(request):
    context = {}
    return render(request, 'store/menu.html', context)


# promo page
def promo(request):
    context = {}
    return render(request, 'store/promo.html', context)


# cart page
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


# checkout page
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

