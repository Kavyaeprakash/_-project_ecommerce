from django.http import JsonResponse
from django.shortcuts import render
from common.models import Seller
from seller.decorators import auth_seller

from seller.models import Product

# Create your views here.
def sel_login(request):
    return render(request,'seller/sel_login.html')

def sel_signup(request):
    return render(request,'seller/sel_signup.html')


def sel_home(request):
    return render(request,'seller/sel_home.html')

def add_product(request):
    msg = ''
    if request.method=='POST':
        pname=request.POST['p_name']
        pdescription=request.POST['p_description']
        pcategory=request.POST['p_category']
        pnumber=request.POST['p_number']
        pstock=request.POST['p_stock']
        pprice=request.POST['p_price']
        pimage=request.FILES['p_image']

        product=Product(
            product_name=pname,
            product_description=pdescription,
            product_category=pcategory,
            product_no=pnumber,
            product_stock=pstock,
            product_price=pprice,
            product_image=pimage,
            seller_id=request.session['sid'])
        product.save()

        msg = 'product added successfully'
    return render(request,'seller/add product.html',{'message':msg})    


    

def master_seller(request):
    return render(request,'seller/master_seller.html')

def update_stock(request):
    products = Product.objects.filter(seller = request.session['sid']).values('id','product_name')
    
    return render(request,'seller/update_stock.html',{'products':products})

def change_password(request):
    msg = ''
    if request.method == 'POST':
        oldpassword = request.POST['old_password']
        newpassword = request.POST['new_password']
        try:

            Seller.objects.filter(id=request.session['sid']).update(s_password=newpassword)
            msg = 'password updated'
        except:
            msg = 'password does not match'

            
        # seller = Seller.objects.get(id=request.session['sid'])
        # if seller.s_password == oldpassword :
        #     seller.s_password=newpassword
        #     seller.save()
        #     msg = 'password updated'
        # else :
        #     msg = 'password does not match'
    return render(request,'seller/change_password.html',{'password_message':msg})



def view_product(request):
    sellerid = request.session['sid']
    product = Product.objects.filter(seller_id=sellerid)
    
    return render(request,'seller/view_product.html',{'products':product})


@auth_seller
def seller_profile(request):
    seller = Seller.objects.get(id = request.session['sid'])
    return render(request,'seller/seller_profile.html',{'seller_profile':seller})

def stock_update(request):
    product_id = request.POST['product_id']
    product = Product.objects.filter(id = product_id).values('product_stock')
    current_stock = product[0]['product_stock']
    
    return JsonResponse({'stock':current_stock})