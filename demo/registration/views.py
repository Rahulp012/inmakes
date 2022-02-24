from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        us = request.POST['t1']
        pa = request.POST['t5']
        user=auth.authenticate(username=us,password=pa)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid register")
            return redirect('login')
    return render(request,"login.html")




# Create your views here.
def register(request):
    if request.method== 'POST':
        us = request.POST['t1']
        fs = request.POST['t2']
        ls = request.POST['t3']
        em = request.POST['t4']
        pa = request.POST['t5']
        cp = request.POST['t6']
        if pa==cp:
            if User.objects.filter(username=us).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.info(request, "email all ready exists")
                return redirect('register')
            else:
                user1=User.objects.create_user(username=us, password=pa, first_name=fs, last_name=ls, email=em)
                user1.save();
                return redirect('login')

        else:
             messages.info(request,"password doesnot matching")
             return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')