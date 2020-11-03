from django.http import HttpResponse
from django.shortcuts import redirect


# checks whether the user is logged in and control accessing to register page
def unauthenticated_user(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return views_func(request, *args, **kwargs)

    return wrapper_func

# allowed user filtration
def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator()
