from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class registermodel(User):
    age=models.IntegerField()
    li=[['Male','MALE'],['Female','FEMALE']]
    gender=models.CharField(max_length=10,choices=li)
    phone=models.BigIntegerField(unique=True)
    address=models.CharField(max_length=150)
    
    
        
    
    
    
