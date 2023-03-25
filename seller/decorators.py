from django.http import HttpResponseRedirect 
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def auth_seller(func) :
    def wrapper (request, *args, **kwargs):
        if 'sid' not in request.session:
            return redirect('common:seller_login')
        else:
            return func (request, *args, **kwargs)
    return wrapper