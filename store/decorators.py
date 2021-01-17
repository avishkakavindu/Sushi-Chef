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
def allowed_user(allowed_roles=['customer']):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You're not authorized to view this page!" )

        return wrapper_func
    return decorator
