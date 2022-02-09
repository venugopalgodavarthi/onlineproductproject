from django.shortcuts import render,redirect
from authen.forms import registerform
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.

def registerview(request):
    form=registerform()
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data['first_name']
            send_mail(subject="Haii welcome to my online shopping",
                      message="Mr/Ms {}, Thank you for registering in my online shopping".format(user),
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[form.cleaned_data['email']])
            messages.success(request,"Haii, Mr/Ms.{} registeration is successfully".format(user.title()))
            return redirect('/authen/login/')
    return render(request,'register.html',{'form':form})

def loginview(request):
    if request.method=='POST':
        user=request.POST['username']
        pass1=request.POST['password']
        user1=authenticate(username=user,password=pass1)
        res=User.objects.get(username=user1)
        if user1:
            login(request,user1)
            send_mail(subject="Haii welcome to my online shopping",
                      message="Mr/Ms {}, Thank you for login in my online shopping".format(user),
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[res.email])
            messages.success(request,"Haii, Mr/Ms.{} login is successfully".format(user1))
            return redirect('/authen/home/')
        else:
            messages.error(request,"login cerditals is not there")
    return render(request,'login.html')

@login_required(login_url='/authen/login/')
def home(request):
    return render(request,'homepage.html')

@login_required(login_url='/authen/login/')
def logoutview(request):
    logout(request)
    return redirect('/welcome')
    
