from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,ContactForm,BlogForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Blogger,Blog
from django.contrib.auth.models import User,Group
from django.contrib.auth.models import User

# Create your views here.

def Home(request):
    blogs=Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def About(request):
    return render(request,'about.html')

def User_SignUp(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Successfully Registered')
            print("Form is Validated...")
            user = fm.save()
            group = Group.objects.get(name='OJAS_BLOG')
            user.groups.add(group)
    else:
        fm=SignUpForm()
    return render(request,'signup.html',{"form":fm})


def User_Login(request):
    print(request.user)
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                un=fm.cleaned_data['username']
                up=fm.cleaned_data['password']
                user=authenticate(username=un,password=up)

                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')

                    return HttpResponseRedirect('/home/pro')

        else:
            fm=AuthenticationForm()
        return render(request,'login.html',{"form":fm})
    else:
        return HttpResponseRedirect('/home/home')



def User_Logout(request):
  logout(request)
  messages.success(request,"Successfully Logout")
  return HttpResponseRedirect('/home/login')



def Contact(request):
    if request.method=='POST':
        fm=ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            print("Form is Validated")
            return HttpResponseRedirect('/home/thanks')

    else:
        fm=ContactForm()
    return render(request,'contact.html',{"form":fm})

def Thanks(request):
    return render(request,'thanks.html')

def add_Blogs(request):
    if request.method == 'POST':
        fm=BlogForm(request.POST)
        if fm.is_valid():
            print('Form is Validated')
            ti=fm.cleaned_data['title']
            des=fm.cleaned_data['description']


            ob=Blog(title=ti,description=des)
            ob.save()
            fm=BlogForm()

            ob1=Blog.objects.all()
            return HttpResponseRedirect('/home/home',{"form":fm,"ob1":ob1})
    else:
        fm=BlogForm()
    ob1 = Blog.objects.all()


    return render(request,'add_blog.html',{"form":fm,"ob1":ob1})


def update_Blogs(request,id):
    if request.method=='POST':
        ab=Blog.objects.get(pk=id)
        fm=BlogForm(request.POST,instance=ab)

        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/home/add')

    else:
        ab=Blog.objects.get(pk=id)
        fm=BlogForm(instance=ab)
    return render(request,'update_blog.html',{"form":fm})


def delete_Blogs(request,id):
    if request.method=='POST':
        ab=Blog.objects.get(pk=id)
        ab.delete()

    return HttpResponseRedirect('/home/add')

def User_Profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/home/log')


