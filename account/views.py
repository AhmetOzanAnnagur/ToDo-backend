from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from account.models import CustomUser

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error": "username or password is wrong"
            })
            
    return render(request, "account/login.html")


def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        if password == repassword:
            if CustomUser.objects.filter(username=username).exists():
                return render(request, "account/register.html",
                            {
                                "error": "This user name has already been taken",
                                "username": username,
                                "email": email,
                                "firstname": firstname,
                                "lastname": lastname
                            })   
            else:
                if CustomUser.objects.filter(email=email).exists():
                    return render(request, "account/register.html",
                                {
                                    "error": "This email has already been taken",
                                    "username": username,
                                    "email": email,
                                    "firstname": firstname,
                                    "lastname": lastname  
                                })
                else:
                    user = CustomUser.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)   
                    user.save()
                    return redirect("login")
        else:
            return render(request, "account/register.html", {"error": "password confirmation does not match"})     
    return render(request, "account/register.html")


def logout_request(request):
    logout(request)
    print(request)
    return redirect("home")