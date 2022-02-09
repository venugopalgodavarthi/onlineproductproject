from django.urls import path
from carts import views
from django.conf.urls.static import static
from django.conf import settings
app_name='carts'
urlpatterns=[
    path('cartindex/',views.cartview,name="cartindex"),
    path('cartlist/<custid>/<lpid>/<lname>/<lmodelno>/<lprice>/<ldiscount>/',views.cartlist,name="cartlist"),
    path('cancelitem/<pk>/',views.cancelitem,name="cancelitem"),
    path('bill/',views.billing,name="bill"),
    path('confirmbill/',views.confirmbill,name="confirmbill"),
    path('buyconfirm/',views.buyconfirm,name="buyconfirm"),
    path('buylist/<custid>/<lpid>/<lname>/<lmodelno>/<lprice>/<ldiscount>/',views.buylist,name="buylist"),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


