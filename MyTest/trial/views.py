from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib import auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import computer,Cars
from .forms import Computerform,NewUserForm,Carsform
import sqlite3

# Create your views here.
def homepage(request):
    return render(request=request,template_name="index.html")

def home(request):
    return render(request=request,template_name="home.html")


#registration view
def register_request(request):
    if request.method=="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Registration successful")
            return redirect(login_user)
    form=NewUserForm()
    return render(request=request,template_name="register.html",context={"register_form":form})


#login view
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
   
    if request.GET:
        username = request.GET['username']
        password = request.GET['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
                redirect(homepage)
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return render(request=request,template_name='new login.html')

def logout(request):
    auth.logout(request)
    return render(request,'new login.html')


#computer
def Adding_Computer(request):
    if request.method=='POST':
        computer_form=Computerform(request.POST,request.FILES)
        if computer_form.is_valid():
            computer_form.save()
            messages.success(request,('your computer is successful added'))
        else:
            messages.error(request,('your data is invalid,try again'))
    computer_form=Computerform()
    return render(request=request,template_name='computer.html',context={'computer_form':computer_form})

#listing computer
def computer_list(request):
    computers=computer.objects.all()
    return render(request=request,template_name='computer_view.html',context={'computers':computers})

#deleating computer
def deletecomputer(request,id):
    Computer=computer.objects.get(id=id)
    Computer.delete()
    return render(request=request,template_name='computer_view.html',context={'Computer':Computer})


#cars
def Adding_Cars(request):
    if request.method=='POST':
        Cars_form=Carsform(request.POST,request.FILES)
        if Cars_form.is_valid():
            Cars_form.save()
            messages.success(request,('your car is successful added'))
        else:
            messages.error(request,('your data is invalid try again'))
    Cars_form=Carsform()
    return render(request=request,template_name='cars.html',context={'Cars_form':Cars_form})

#listing cars
def Cars_list(request):
    car=Cars.objects.all()
    return render(request=request,template_name="cars_view.html",context={'car':car})
#deleating car
def deletecar(request,id):
    Car=Cars.objects.get(id=id)
    Car.delete()
    return render(request=request,template_name="cars_view.html",context={'Car':Car})

#def updatecar(request,id):
   # cars=Cars.objects.get(id=id)
    #return render(request=request,template_name="carupdate.html",context={'cars':cars})


#def updatecarrecord(request,id):
   #  carname=request.POST['carname']
    #manufacture=request.POST['manufacture']
    #enginetype=request.POST['enginetype']
    #color=request.POST['color']
    #automation=request.POST['automation']
    #speed=request.POST['speed']
    #price=request.POST['price']
    #Carr=Cars.objects.get(id=id)
    #Car.car_name=carname
    #Car.manufacture=manufacture
    #Car.engine_type=enginetype
    #Car.color=color
    #Car.automation=automation
    #Car.speed=speed
    #Car.price=price
    #Car.save()
    #return HttpResponseRedirect(reverse('homepage'))


