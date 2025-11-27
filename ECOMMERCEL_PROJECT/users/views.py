from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import UserProfile  


class RegisterView(View):
    def get(self, request):
        return render(request, "users/register.html")

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render("users/register.html",{"error":"this username already taken"})

        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

       
        user_profile = UserProfile.objects.create(user=user)
        user_profile.save()

        return redirect("users:login")  


class LoginViewCustom(View):
    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("products:product-list")  
        else:
            return render(request, "users/login.html", {"error": "Invalid credentials"})


def logout_view(request):
    logout(request)
    return redirect("products:product-list")
