from django.contrib import admin
from carts.models import cartmodel
# Register your models here.

class admincartmodel(admin.ModelAdmin):
    list_display= ['coid','cocustid','coprodid','copname','comodelid','coprice','codiscount']
    
admin.site.register(cartmodel,admincartmodel)
