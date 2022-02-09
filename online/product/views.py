from django.shortcuts import render
from product.models import mobiledetail
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/authen/login/')
def productview(request):
    res=mobiledetail.objects.all()
    return render(request,'productindex.html',{'res':res})
