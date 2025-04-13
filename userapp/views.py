from django.shortcuts import render,redirect
from .models import *
from datetime import date
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def registerview(request):
    name=request.POST['name']
    username=request.POST['username']
    phone=request.POST['ph']
    image=request.FILES['image']
    address=request.POST['addr']
    password=int(request.POST['password'])
    data=Data(name=name, address=address, phone=phone, image=image, username=username)
    data.save()
    
    data1=Login(username=username,password=password,type=1)
    data1.save()  
    return render(request,"register.html")


def register(request):
    return render(request,"register.html")

def loginaccount(request):
    data=Data.objects.all()
    data1=Login.objects.all()
    return render(request,"registerview.html",{'result':data ,'result1':data1})
        
def login(request):
    return render(request,"login.html")


def deleteData(request,id):
    d=Data.objects.get(id=id)
    d.delete()
    return redirect("/")

def user(request):
    return render(request,"user.html",{})

def deleteUser(request,id):
    u=Login.objects.get(id=id)
    u.delete()
    return redirect("/")

def admin(request):
    return render(request,"adminn.html")


def check(request):
    username=(request.POST["username"])
    password=(request.POST["password"])
    data1=Login.objects.get(username=username,password=password)
    if data1.type==1:
      request.session["username"]=data1.username
      productdata=Product.objects.all()
      return render(request,"user.html",{'result2':productdata})
    elif data1.type==0:
       request.session["username"]=data1.username
       return render(request,"adminn.html")
   
def product(request):
    return render(request,"product.html")

def productview(request):
    productname=request.POST['productname']
    description=request.POST['description']
    price=request.POST['price']
    photo=request.FILES['photo']
    productdata=Product(productname=productname, description=description, price=price, photo=photo,)
    productdata.save()  
    return render(request,"product.html")

def productdisplay(request):
    productdata=Product.objects.all()
    return render(request,"productview.html",{'result2':productdata})

def deleteProduct(request,id):
    p=Product.objects.get(id=id)
    p.delete()
    return redirect("/")

# buynow profile 


def buy(request):
    username=request.session["username"]
    productname=request.POST['productname']
    today=date.today()
    shop=Data.objects.get(username=username)
    shoppro=Product.objects.get(id=productname)
    data3=Buy(username=shop,productname=shoppro,date=today)
    data3.save()
    data3=Product.objects.all()
    messages.success(request,"product is buyed")
    return render(request,"user.html",{'result2':data3})

def myprofile(request):
    a=request.session["username"]
    data=Data.objects.get(username=a)
    return render(request,"myprofile.html",{'result':data})

def logoutuser(request):
    logout(request)
    return redirect('login')

def myorder(request):
    a=request.session["username"]
    shop=Data.objects.get(username=a)
    data4=Buy.objects.filter(username=shop)
    return render(request,"myorder.html",{'result3':data4})

def deleteorder(request,id):
    order=Buy.objects.get(id=id)
    order.delete()
    return redirect("/")

def updateData(request,pk):
    edit=Data.objects.get(id=pk)
    if request.method =="POST":
       edit.image=request.FILES.get('image')
       edit.name=request.POST.get('name')
       edit.address=request.POST.get('addr')
       edit.phone=request.POST.get('ph')
       edit.username=request.POST.get('username')
       edit.save()
       messages.success(request,"product updated successfully ")
    context={'edit':edit}
    return render(request,"edit.html",context)


        