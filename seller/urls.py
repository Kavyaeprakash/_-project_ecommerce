from django.urls import path
from . import views
app_name="seller"
urlpatterns=[
    path('sel_login', views.sel_login),
    path('sel_signup', views.sel_signup),
    path('sel_home', views.sel_home,name='s_home'),
    path('masterseller', views.master_seller,name='master_seller'),
    path('addproduct', views.add_product,name='add_product'),
    path('updatestock', views.update_stock,name='update_stock'),
    path('changepassword', views.change_password,name='change_password'),
    path('viewproduct', views.view_product,name='view_product'),
    path('sellerprofile', views.seller_profile,name='seller_profile'),






]
