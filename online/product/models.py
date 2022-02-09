from unicodedata import category
from django.db import models

# Create your models here.

class productitem(models.Model):
    itemid=models.BigAutoField(primary_key=True)
    itemname=models.CharField(max_length=50)
    def __str__(self):
        return self.itemname
    
class mobilecompany(models.Model):
    comyid=models.BigAutoField(primary_key=True)
    comyname=models.CharField(max_length=50)
    def __str__(self):
        return self.comyname
    
class mobiledetail(models.Model):
    mid=models.BigAutoField(primary_key=True)
    item=models.ForeignKey(productitem,on_delete=models.CASCADE)
    company=models.ForeignKey(mobilecompany,on_delete=models.CASCADE)
    mname=models.CharField(max_length=50)
    mmodelno=models.CharField(max_length=15)
    mdesc=models.TextField(max_length=500)
    imei=models.BigIntegerField()
    mprice=models.FloatField()
    mdiscount=models.FloatField()
    quantity=models.IntegerField()
    mimg=models.ImageField(upload_to='product')
    def __str__(self):
        return self.mname
    
    
class clothcompany(models.Model):
    ccomid=models.BigAutoField(primary_key=True)
    ccomname=models.CharField(max_length=50)
    def __str__(self):
        return self.ccomname
    
    
class clothtype(models.Model):
    ctid=models.BigAutoField(primary_key=True)
    ctname=models.CharField(max_length=50)
    def __str__(self):
        return self.ctname
    
class clothdetail(models.Model):
    cid=models.BigAutoField(primary_key=True)
    citem=models.ForeignKey(productitem,on_delete=models.CASCADE)
    ccompany=models.ForeignKey(mobilecompany,on_delete=models.CASCADE)
    cname=models.CharField(max_length=50)
    cmodelno=models.CharField(max_length=15)
    cdesc=models.TextField(max_length=500)
    ctype=models.ForeignKey(clothtype,on_delete=models.CASCADE)
    lu=[['Male','MALE'],['Female','FEMALE'],['kids','KIDS']]
    category=models.CharField(max_length=15,choices=lu)
    cprice=models.FloatField()
    cdiscount=models.FloatField()
    quantity=models.IntegerField()
    li=[['Small','SMALL'],['Medium','MEDIUM'],['Large','LARGE'],['ExtraLarge','EXTRALARGE'],['DoubleExtra Large','DOUBLEEXTRA LARGE']]
    size=models.CharField(max_length=25,choices=li)
    cimg=models.ImageField(upload_to='cloths')
    def __str__(self):
        return self.cname
    
class grocaryitems(models.Model):
    gid=models.BigAutoField(primary_key=True)
    gitem=models.CharField(max_length=50)
    
    def __str__(self):
        return self.gitem
    
class grocarydetail(models.Model):
    gid=models.BigAutoField(primary_key=True)
    gitem=models.ForeignKey(productitem,on_delete=models.CASCADE)
    gcompany=models.ForeignKey(mobilecompany,on_delete=models.CASCADE)
    groitem=models.ForeignKey(grocaryitems,on_delete=models.CASCADE)
    gname=models.CharField(max_length=50)
    gdesc=models.TextField(max_length=500)
    gprice=models.FloatField()
    gdiscount=models.FloatField()
    quantity=models.IntegerField()
    gimg=models.ImageField(upload_to='grocary')
    def __str__(self):
        return self.gname

    
    
    
