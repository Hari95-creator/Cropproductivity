"""cropproduction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from farmers import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addproduct/',views.addproduct),
    path('dashboard/',views.dash),
    path('editproduct/',views.editproduct),
    path('login/',views.login),
    path('loginsignup/',views.loginsignup),
    path('orderdetails/',views.orderdetails),
    path('orderhistory/',views.orderhistory),
    path('orders/',views.orders),
    path('productdetails/',views.productdetails),
    path('signup/',views.signup),

    #public view  path
    path('publicabout/',views.publicabout),
    path('publiccart/',views.publiccart),
    path('changeaddress/',views.changeaddress),
    path('changepassword/',views.changepassword),
    path('publiccheckout/',views.publiccheckout),
    path('publiccontact/',views.publiccontact),
    path('publicindex/',views.publicindex),
    url(r'^$',views.publicindex),#for creating root page 
    path('publiclogin/',views.publiclogin),
    path('publicorderstatus/',views.orderstatus),
    path('publicorderhistory/',views.orderhistory),
    path('farmersdetails/',views.ourfarmersdetails),
    path('farmers/',views.ourfarmers),
    path('publicproduct/',views.publicproduct),
    path('publicshop/',views.publicshop),
    path('publicsignup/',views.publicsignup),
    path('publicwishlist/',views.publicwishlist),
    path('errorpage/',views.errorpage),
    path('publicsoiltest/',views.soiltest),
    path('publicweather/',views.weatherdata),
    url(r'^ajax/autocomplete/$', views.autocomplete, name='ajax_autocomplete'),
    


]
