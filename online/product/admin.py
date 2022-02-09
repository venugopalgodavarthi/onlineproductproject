from django.contrib import admin
from product.models import clothcompany,clothdetail,clothtype,mobilecompany,mobiledetail,grocarydetail,grocaryitems,productitem
# Register your models here.
class mobiledetailsadmin(admin.ModelAdmin):
    list_display=['mid','item','company','mname','mmodelno','mdesc','imei','mprice','mdiscount','quantity','mimg']
admin.site.register(clothcompany)
admin.site.register(clothtype)
admin.site.register(grocaryitems)
admin.site.register(mobilecompany)
admin.site.register(productitem)
admin.site.register(mobiledetail, mobiledetailsadmin)
admin.site.register(grocarydetail)
admin.site.register(clothdetail)