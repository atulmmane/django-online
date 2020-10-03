from django.shortcuts import render,redirect,HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from . models import Category,Product,Cart
from django.contrib.auth.models import User
categoryList=Category.objects.all()
productList=Product.objects.all()

def home(request):
    userName=request.session.get('userName')
    d={"cl":categoryList,'pl':productList,'uname':userName}
    return render(request,"home.html",d)


def addUser(request):
   
    if request.method=='POST':
        u=UserForm(request.POST)
        u.save()
        return redirect("/")
    else:
        u=UserForm
        d={"cl":categoryList,'form':u}
        return render(request,'myform.html',d)

    
def mylogin(request):
    d={"cl":categoryList}

    if request.method=='POST':
        uname=request.POST.get("uname")
        passw=request.POST.get("passw")
        usr=authenticate(request,username=uname,password=passw)
        if usr is not None:
            request.session['userName']=uname
            login(request,usr)
            return redirect("/")
        else:
            return HttpResponse("<h1>Invalid UserName and Passwor</h1>")
    else:
        return render(request,'login.html',d)
    
def logOUT(request):
    logout(request)
    return redirect("/")


def getByCategory(request):
    cid=request.GET.get("cid")
    pl=Product.objects.filter( category_id=cid)
    d={"cl":categoryList,'pl':pl}
    return render(request,'home.html',d)

def serachPage(request):
    d={"cl":categoryList,'pl':productList}
    return render(request,'productSearch.html',d)

def search(request):
    sp=request.POST.get('sp')
    pl=Product.objects.filter(pname__icontains=sp)
    d={"cl":categoryList,'pl':pl}
    return render(request,'productSearch.html',d)

    # name like '%s%'

def addToCart(request):
    id=request.GET.get("id")
    prd=Product.objects.get(id=id)
    userName=request.session.get('userName')
    usr=User.objects.get(username=userName)
    cart=Cart()
    cart.product=prd
    cart.user=usr
    cart.save()
    return redirect("/")

def cartList(request):
    userName=request.session.get('userName')
    usr=User.objects.get(username=userName)
    crlist=Cart.objects.filter(user_id=usr.id)
    totalBill=0
    for b in crlist:
        totalBill=totalBill+b.product.price
    
    d={"cl":categoryList,'crlist':crlist,'totalBill':totalBill}


    return render(request,'cartList.html',d)


def feed(request):
    if request.method=='POST':
        u=UserForm(request.POST)
        u.save()
        return redirect("/")
   
