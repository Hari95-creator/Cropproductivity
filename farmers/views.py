from django.shortcuts import render

# Create your views here.
def addproduct(request):
    return render(request,'farmers/addproduct.html')
def dash(reguest):
    return render(reguest,'farmers/dashboard.html')
def editproduct(request):
    return render(request,'farmers/editproduct.html')
def login(request):
    return render(request,'farmers/login.html')
def loginsignup(request):
    return render(request,'farmers/loginsignupbase.html')
def orderdetails(request):
    return render(request,'farmers/orderdetails.html')
def orderhistory(request):
    return render(request,'farmers/orderhistory.html')
def orders(request):
    return render(request,'farmers/orders.html')
def productdetails(request):
    return render(request,'farmers/productdetails.html')
def signup(request):
    return render(request,'farmers/signup.html')

#functions for public

def autocomplete(request):
    if request.is_ajax():
        queryset = products.objects.filter(pname__icontains=request.GET.get('search', None))
        list = []        
        for i in queryset:
            list.append(i.pname)
        data = {
            'list': list,
        }
        return JsonResponse(data)

def publicabout(request):
    return render(request,'public/about.html')
def publiccart(request):
    return render(request,'public/cart.html')
def changeaddress(request):
    return render(request,'public/change_address.html')
def changepassword(request):
    return render(request,'public/change_password.html')
def publiccheckout(request):
    return render(request,'public/checkout.html')
def publiccontact(request):
    return render(request,'public/contact.html')
def publicindex(request):
    return render(request,'public/index.html')
def publiclogin(request):
    return render(request,'public/login.html')
def orderstatus(request):
    return render(request,'public/order_status.html')
def orderhistory(request):
    return render(request,'public/orderhistory.html')
def ourfarmersdetails(request):
    return render(request,'public/ourfarmers_details.html')
def ourfarmers(request):
    return render(request,'public/ourfarmers.html')
def publicproduct(request):
    return render(request,'public/product.html')
def publicshop(request):
    return render(request,'public/shop.html')
def publicsignup(request):
    return render(request,'public/signup.html')  
def publicwishlist(request):
    return render(request,'public/wishlist.html')
def errorpage(request):
    return render(request,'public/4O4.html')
def soiltest(request):
    return render(request,'public/soiltest.html')
def weatherdata(request):
    return render(request,'public/weather.html')




