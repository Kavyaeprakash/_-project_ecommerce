from django.urls import path
from . import views
app_name = 'common'

urlpatterns = [
    # path('customerlogin', views.customer_login, name='customer_login'),
    path('customersignup', views.cus_signup, name='customer_signup'),
    path('customerlogin', views.customer_login, name='customer_login'),
    path('sellerlogin', views.seller_login, name='seller_login'),
    path('sellersignup', views.seller_signup, name='seller_signup'),
    # path('home', views.home, name='home'),
    path('mastercommon', views.master_common, name='master_common'),
    path('commonhome', views.common_home, name='common_home'),
    path('adminlogin', views.admin_login, name='admin_login'),
    path('emailexist', views.email_exist, name='email_exist'),






]

