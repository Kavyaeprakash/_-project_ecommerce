from django.urls import path
from . import views
app_name='customer'
urlpatterns=[

    path('cus_login', views.cus_login),
    path('cus_signup', views.cus_signup),
    path('cus_home', views.cus_home,name='c_home'),
    path('mastercustomer', views.master_customer,name='master_customer'),
    path('c_logout',views.customer_logout,name='customer_logout'),
    path('productdetails/<int:p_id>', views.product_details,name='product_details'),
    path('mycart', views.my_cart,name='my_cart'),
    path('myorders', views.my_orders,name='my_orders'),
    path('customerprofile', views.customer_profile,name='customer_profile'),
    path('changepassword', views.change_password,name='change_password'),





]