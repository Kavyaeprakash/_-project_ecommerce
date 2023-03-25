from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render,redirect
from random import randint
from .models import Customer, Seller
from django.core.mail import send_mail


# Create your views here.
# def home(request):
#     return render(request,'common/home.html')

def common_home(request):
    return render(request,'common/common home.html')

def admin_login(request):
    return render(request,'common/admin login.html')


def customer_login(request):
    # return render(request,'common/customer login.html')
    msg = ''
    if request.method == 'POST' :
        cusername = request.POST['username']
        cpassword = request.POST['password']
        try :
            customer = Customer.objects.get(c_email = cusername,c_password = cpassword)
            request.session['customer'] = customer.id
            return redirect('customer:c_home')
        except :
            msg = 'invalid credentials'

    return render(request, 'common/customer login.html',{'message':msg})



def seller_login(request):
    msg = ''
    if request.method == 'POST' :
        
        susername = int(request.POST['username'])
        spassword = request.POST['password']
        try :
            seller = Seller.objects.get(s_username=susername,s_password=spassword)
            request.session['sid']=seller.id
            return redirect('seller:s_home')
        except:
            msg = 'Invalid Credentials'
        
    return render(request, 'common/sel_login.html',{'message':msg})


def seller_signup(request):
     msg = ''
     if request.method == 'POST' :
        sname = request.POST['sname']
        smobile = request.POST['smobile']
        semail = request.POST['semail']
        saddress = request.POST['saddress']
        sbankname = request.POST['bankname']
        saccountnumb = request.POST['accountnumber']
        sbankbranch = request.POST['bankbranch']
        sifsccode = request.POST['ifsccode']
        simage = request.FILES['seller_pic']
        susername = randint(1000,9999)
        spassword = 'sel-'+sname.lower()+str(susername)

        seller = Seller(
            s_name = sname,
            s_mobile = smobile,
            s_email = semail,
            s_address = saddress,
            s_bank_name = sbankname,
            s_acc_number = saccountnumb,
            s_bank_branch = sbankbranch,
            s_ifsc_code = sifsccode,
            s_image = simage,
            s_username = susername,
            s_password = spassword)
        seller.save()

        msg = 'seller registered successfully'
        subject = 'account name and password'
        message = 'hai your username is '+str(susername)+'and your password is '+spassword
        email_from = settings.EMAIL_HOST_USER
        send_mail(
            subject,
            message,
            email_from,
            [semail],
            fail_silently = False
        )

     return render(request,'common/sel_signup.html',{'message':msg})
            
    
def email_exist(request):
    email = request.POST['email_data']
    email_exist= Customer.objects.filter(c_email =email).exists()
    return JsonResponse({'email_exist':email_exist})


def master_common(request):
    return render(request,'common/master common.html')
    

def cus_signup(request):
    # return render(request, 'common/cus_signup.html')
    msg = ''

    if request.method == 'POST' :
        cname = request.POST['customer name']
        cemail = request.POST['email']
        cmobile = request.POST['mobile no']
        caddress = request.POST['address']
        cgender = request.POST['gender']
        cpassword = request.POST['password']

        try:
            new_customer = Customer(
                c_name = cname, 
                c_email = cemail, 
                c_mobile = cmobile,
                c_address = caddress, 
                c_gender = cgender,
                c_password = cpassword
                )
            new_customer.save()
            msg = 'successfully registered'
        except:
            msg = 'invalid credentials'


    return render(request, 'common/cus_signup.html', {'message':msg})

