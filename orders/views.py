from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'orders/home.html')

def register(request):

    first = request.POST["first"]
    surname = request.POST["surname"]
    email = request.POST["email"]
    username = request.POST["username"]
    password = request.POST["password"]

    # user = User.objects.create_user(first, surname, email, username, password)

    return render(request, 'orders/register.html')

def log_in(request):

    username = request.POST["un"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "users/login.html", {"message": "Invalid username/password."})

    return render(request, 'orders/login.html')

def log_out(request):

    logout(request)
    return render(request, 'orders/login.html', {'message': 'Successfully logged out!'})

def menu(request):
    return render(request, 'orders/menu.html')

def basket(request):
    return render(request, 'orders/basket.html')
