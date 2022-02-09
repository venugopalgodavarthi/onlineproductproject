from django.http import HttpResponse
from django.shortcuts import render,redirect
from carts.models import cartmodel, payment,purchase,cartdetails,parchasedetails
from product.models import mobiledetail
from django.db.models import Count,Sum,Max
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/authen/login/')
def cartview(request):
    res=cartmodel.objects.all()
    count=cartmodel.objects.all().aggregate(Count('coid'))
    sum1=cartmodel.objects.all().aggregate(Sum('coprice'))
    return render(request,'cartindex.html',{'res':res,'count':count['coid__count'],'sum':sum1['coprice__sum']})

@login_required(login_url='/authen/login/')
def cartlist(request,custid,lpid,lname,lmodelno,lprice,ldiscount):
    cartmodel.objects.create(cocustid_id=custid,coprodid=lpid,copname=lname,comodelid=lmodelno,coprice=lprice,codiscount=ldiscount)
    return redirect('/product/productview/')

@login_required(login_url='/authen/login/')
def cancelitem(request,pk):
    res=cartmodel.objects.get(coid=pk).delete()
    return redirect('/carts/cartindex/')

details=""
@login_required(login_url='/authen/login/')
def billing(request):
    global details
    if request.method=="POST":
        res=cartmodel.objects.all()
        count=cartmodel.objects.all().aggregate(Count('coid'))
        sum1=cartmodel.objects.all().aggregate(Sum('coprice'))
        details=request.POST
        return render(request,"billpage.html",{'res':res,'count':count['coid__count'],'sum':sum1['coprice__sum'],'d':details})

@login_required(login_url='/authen/login/')
def confirmbill(request):
    if request.method=="POST":
        print("haii")
        cart=cartmodel.objects.all().values('coprodid','copname','comodelid','coprice','codiscount')
        print(cart)
        res=cartmodel.objects.all().values_list('cocustid')
        print(res)
        sum1=cartmodel.objects.all().aggregate(Sum('coprice'))
        print(sum1)
        payment.objects.create(
            cafirst=details['username'], caphone=details['phone'], caemail=details['email'], caaddress1=details['address1'],
            caaddress2=details['address2'], cacountry=details['country'], castate=details['state'], capin=details['pincode'],
            cashippingbill=details['same-address'], paytype=details['paymentMethod'], paycname=details['cardname'], paycno=details['cardno'],
            payexpr=details['expr'], paycvv=details['cvv'], pcustid_id=list(set(res))[0][0], ptotal=sum1['coprice__sum'])
        pu=purchase.objects.all().aggregate(Max("pid"))['pid__max']
        print(pu)
        for i in cart:
            parchasedetails.objects.create(pdid_id=pu, coprodid=i['coprodid'], 
                                           copname=i['copname'], comodelid=i['comodelid'],
                                           coprice=i['coprice'], codiscount=i['codiscount'],pucustid=list(set(res))[0][0])
        cartmodel.objects.all().delete()
        return redirect('/authen/home/')
    return redirect("/carts/cardindex")

buydetails=""
productdetails=""
@login_required(login_url='/authen/login/')
def buylist(request,custid,lpid,lname,lmodelno,lprice,ldiscount):
    global buydetails,productdetails
    details=[custid,lpid,lname,lmodelno,lprice,ldiscount]
    productdetails=details
    if request.method=="POST":
        buydetails=request.POST
        return render(request,"buypage.html",{'b':details,'d':request.POST})
    return render(request,"buycart.html",{'d':details})


def buyconfirm(request):
    if request.method=="POST":
        print("haii")
        payment.objects.create(
            cafirst=buydetails['username'], caphone=buydetails['phone'], caemail=buydetails['email'], caaddress1=buydetails['address1'],
            caaddress2=buydetails['address2'], cacountry=buydetails['country'], castate=buydetails['state'], capin=buydetails['pincode'],
            cashippingbill=buydetails['same-address'], paytype=buydetails['paymentMethod'], paycname=buydetails['cardname'], paycno=buydetails['cardno'],
            payexpr=buydetails['expr'], paycvv=buydetails['cvv'], pcustid_id=int(productdetails[0]), ptotal=productdetails[4])
        pu=purchase.objects.all().aggregate(Max("pid"))['pid__max']
        print(pu)

        print(productdetails)
        print(type(productdetails))
        parchasedetails.objects.create(pdid_id=pu, coprodid=int(productdetails[1]),pucustid_id=int(productdetails[0]),
                                           copname=productdetails[2], comodelid=productdetails[3],
                                           coprice=float(productdetails[4]), codiscount=float(productdetails[5]))
        return redirect('/authen/home/')
    return redirect("/product/productview")