from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from WebApp.models import ItemsList
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


def Home(request):
    return render (request,'MyApp/home.html')


def Register(request):
    if request.method=='POST':
        firstname=request.POST["fname"]
        lastname = request.POST["lname"]
        username = request.POST["uname"]
        email = request.POST["email"]
        password1= request.POST["pasword1"]
        password2=request.POST['pasword2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('/reg/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('/reg/')
            else:
                user=User.objects.create_user(first_name=firstname,password=password1,last_name=lastname,username=username,email=email)
        #user.set_password(password)
                user.save()
                print("user created")


        else:
            print("password not matched")
            return redirect('/reg/')
        return redirect("/login/")
    else:
        return render(request,'MyApp/register.html')


def Login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/success/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("/")
    else:
        return render(request,'MyApp/login.html')

def Success(request):
    context={}
    context["user"]=request.user
    return render(request,'MyApp/success.html',context)


def logout_kc(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required(login_url='/login/')
def Items(request):
    obj=ItemsList.objects.all()
    return render(request,'MyApp/item.html',{'obj':obj})

def create(request):
    return render(request,'MyApp/create.html')

def Cook(request):
    print(request.FILES)
    ItemsList.objects.create(itemname=request.POST["iname"],
                             ingredients=request.POST["ingredients"],
                             process=request.POST["process"],
                             image=request.FILES["image"])
    return HttpResponseRedirect('/item/')

@login_required(login_url='/login/')
def detail(request,id=None):
    jk= ItemsList.objects.get(id=id)
    return render(request,'MyApp/details.html',{'jk':jk})


def delete(request,id=None):
    ItemsList.objects.get(id=id).delete()
    return HttpResponseRedirect('/item/')

