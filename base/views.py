from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def signuppage(request):
    error_messages = {
        'pass_error':'Password not match',
        'email_error':'Email already exists',
        'name_error':'Username already exists'
    }
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("passwprd1")
        pass2 = request.POST.get("password2")

        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.error(request,error_messages["email_error"])
            elif User.objects.filter(username=username).exists():
                messages.error(request,error_messages["name_error"])
            else:
                myuser = User.objects.create_user(username,email,pass1)
                myuser.save()
                return redirect("loginpage")
        else:
            messages.error(request,error_messages["pass_error"])
    return render(request,"signup.html")

def loginpage(request):
    error_messages = {
        'error':'Invalid Username or Password'
    }
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("homepage")
        else:
            messages.error(request,error_messages["error"])
    return render(request,"login.html")
def homepage(request):
    return render(request,"home.html")