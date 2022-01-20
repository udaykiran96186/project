
from django.shortcuts import redirect, render
from app1.forms import CreateAccountForm,UserForm
from django.contrib import messages
# from django.contrib.auth import login
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm


def homeview(request):
    return render(request,"home.html")

def CreateAccountView(request):
    form = CreateAccountForm()
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Dear, {form.cleaned_data['firstName']}, it takes some time to activate your Bank account,kindly refer to Check your status after 24hr")
            return redirect("home")

    context = {
        "form":form
    }
    return render(request,"createAccountForm.html",context)

def loginView(request):
    form = UserForm()
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_superuser:
            auth.login(request,user)
            messages.info(request,"useranme and password  match")
            return redirect("home")
        else:
            messages.info(request,"useranme and password not match")
            return redirect("login")
    else:
        return render(request,"login.html",{"form":form})

    # if request.method == "POST" and formlogin.is_valid():
    #     formlogin = LoginForm(request.POST or None)
    #     userName = formlogin.cleaned_data.get("userName")
    #     password = formlogin.cleaned_data.get("password")
    #     print(userName)
    #     user = auth.authenticate(username=userName,password=password)
    #     if user is not None:
    #         print("hiiii")
    #         user.login(request.user)
    #         print("ggg")
    #         return redirect("home")
    #     else:
    #         print("hi")
    #         messages.info(request,"useranme and password not match")
    #         return redirect("login")
    # else:
    #     context = {
    #         "form":formlogin
    #     }
    #     return render(request,"login.html",context)


def registerUser(request):
    # form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect("home")
    else:
        form = UserCreationForm()
        messages.success(request, 'Account not successfully')
        context = {
            'form':form
        }
        return render(request,"first.html",context)
