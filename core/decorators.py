from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden


def login_and_role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if required_role == "customer" and not user.is_customer:
                return HttpResponseForbidden("You are not authorized to access this page1.")
            
            if required_role == "seller" and not user.is_seller:
                return HttpResponseForbidden("You are not authorized to access this page2.")
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator