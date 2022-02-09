from django.urls import path
from product import views
from django.conf.urls.static import static
from django.conf import settings
app_name='product'
urlpatterns=[
    path('productview/',views.productview,name="productview")
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

