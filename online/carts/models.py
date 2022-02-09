from django.utils import timezone
from django.db import models
from authen.models import registermodel
from product.models import mobiledetail,grocarydetail,clothdetail
#from django.contrib.auth.models import User
from authen.models import registermodel
# Create your models here.

class cartmodel(models.Model):
    coid=models.AutoField(primary_key=True)
    cocustid=models.ForeignKey(registermodel,on_delete=models.CASCADE) #cocustid_id
    coprodid=models.IntegerField()
    copname=models.CharField(max_length=50)
    comodelid=models.CharField(max_length=30)
    coprice=models.FloatField()
    codiscount=models.FloatField()
    

class cartdetails(models.Model):
    caid=models.BigAutoField(primary_key=True)
    cafirst=models.CharField(max_length=50)
    caphone=models.BigIntegerField()
    caemail=models.EmailField(max_length=50)
    caaddress1=models.TextField()
    caaddress2=models.TextField()
    cacountry=models.CharField(max_length=25)
    castate=models.CharField(max_length=25)
    capin=models.IntegerField()
    cashippingbill=models.BooleanField(default=False)

class purchase(cartdetails):
    pid=models.BigAutoField(primary_key=True)
    pdate=models.DateTimeField(default=timezone.now)
    pcustid=models.ForeignKey(registermodel,on_delete=models.CASCADE)
    ptotal=models.FloatField()
    
class payment(purchase):
    paytype=models.CharField(max_length=50)
    paycname=models.CharField(max_length=50)
    paycno=models.BigIntegerField()
    payexpr=models.CharField(max_length=10)
    paycvv=models.CharField(max_length=5)
        
class parchasedetails(models.Model):
    pdid=models.ForeignKey(purchase,on_delete=models.CASCADE)
    pucustid=models.ForeignKey(registermodel,on_delete=models.CASCADE)
    coprodid=models.IntegerField()
    copname=models.CharField(max_length=50)
    comodelid=models.CharField(max_length=30)
    coprice=models.FloatField()
    codiscount=models.FloatField()
    pdate=models.DateTimeField(default=timezone.now)
    
