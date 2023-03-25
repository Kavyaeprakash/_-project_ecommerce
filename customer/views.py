from itertools import product
from django.http import JsonResponse
from django.shortcuts import redirect, render

from common.models import Customer
from customer.decorators import auth_customer
from customer.models import Cart
from seller.models import Product

# Create your views here.
def cus_login(request):
    return render(request,'customer/cus_login.html')
def cus_signup(request):
    return render(request,'customer/cus_signup.html')


@auth_customer
def cus_home(request):
    customer = Customer.objects.get(id = request.session['customer'])
    products=Product.objects.all()
    return render(request,'customer/cus_home.html',{'customer_data':customer,'product_data':products})

def customer_logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:common_home')



def master_customer(request):
    return render(request,'customer/master_customer.html')

def product_details(request,p_id):
    msg = ''
    product=Product.objects.get(id = p_id)
    if request.method == 'POST' :
        cart_exist = Cart.objects.filter(product = p_id, customer = request.session['customer']).exists()

        if not cart_exist:
            cart = Cart(customer_id = request.session['customer'], product_id = p_id)
            cart.save()
            return redirect('customer:my_cart')
        else:
            msg = 'item already in cart'
    
    return render(request,'customer/product details.html',{'product':product,'msg':msg})

def my_cart(request):
    
    customerid = request.session['customer']
    
    cart_items = Cart.objects.filter(customer = customerid)
    
    return render(request,'customer/my_cart.html',{'cart_items':cart_items})

def my_orders(request):
    return render(request,'customer/my_orders.html')




@auth_customer
def customer_profile(request):
    customer = Customer.objects.get(id = request.session['customer'])
    return render(request,'customer/customer_profile.html',{'customer_profile':customer})

def change_password(request):
    msg = ''
    if request.method == 'POST':
        oldpassword = request.POST['old_password']
        newpassword = request.POST['new_password']
        try:

            Customer.objects.filter(id=request.session['customer']).update(c_password=newpassword)
            msg = 'password updated'
        except:
            msg = 'password does not match'

    return render(request,'customer/change_password.html',{'password_msg':msg})

def change_quantity(request):
    error_msg = "#success_msg ="
    quantity = int(request.POST['quantity'])
    product_id = int(request.POST['product_id'])
    current_stock = Product.objects.get(id = product_id).product_stock
    if quantity>current_stock:
        error_msg = 'out of stock'
    else:
        error_msg = 'in stock'

    return JsonResponse ({'error_msg':error_msg})