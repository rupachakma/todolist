from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login

from base.models import Tasklist

# Create your views here.
def signuppage(request):
    if request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("loginpage")
        else:
            return redirect("signuppage")
    else:
        form = UserCreationForm()
    return render(request,"signup.html",{'form':form})

def loginpage(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("homepage")
            else:
                return redirect("loginpage")
    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form':form})

def homepage(request):
    return render(request,"home.html")

