from django.shortcuts import render


def about(request):
    return render(request, 'store/about.html')