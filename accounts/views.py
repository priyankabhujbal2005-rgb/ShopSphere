from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists."
            })

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect("/")

    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("/")

        return render(request, "login.html", {
            "error": "Invalid username or password."
        })

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/")
