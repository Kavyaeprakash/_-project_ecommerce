from django.http import HttpResponseRedirect 
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied





def divide_dec(func):
    def wrapper(a,b):
        if b > a:
            a,b = b,a
            return func(a,b)
    return wrapper




@divide_dec
def divide(a,b):
    result = a/b
    print(result)

divide(2,10)

def auth_customer(func) :
    def wrapper (request, *args, **kwargs):
        if 'customer' not in request.session:
            return redirect('common:customer_login')
        else:
            return func (request, *args, **kwargs)
    return wrapper