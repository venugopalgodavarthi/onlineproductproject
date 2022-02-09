from django.urls import path
from authen import views
from django.conf.urls.static import static
from django.conf import settings
app_name='authen'
urlpatterns=[
    path('register/',views.registerview,name="register"),
    path('login/',views.loginview,name="login"),
    path('home/',views.home,name="home"),
    path('logout/',views.logoutview,name="logout"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

