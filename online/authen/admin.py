from django.contrib import admin
from authen.models import registermodel
# Register your models here.

class registeradmin(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name','age','gender','email','phone','address']
admin.site.register(registermodel,registeradmin)