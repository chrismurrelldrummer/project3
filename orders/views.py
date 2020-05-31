from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

# from django.contrib.auth import authenticate
# user = authenticate(username='john', password='secret')
# if user is not None:
#     # A backend authenticated the credentials
# else:
#     # No backend authenticated the credentials

def home(request):
    return render(request, 'orders/home.html')

def register(request):
    return render(request, 'orders/register.html')

def log_in(request):
    return render(request, 'orders/login.html')

def log_out(request):
    return render(request, 'orders/login.html', {'message': 'Successfully logged out!'})

def menu(request):
    return render(request, 'orders/menu.html')

def basket(request):
    return render(request, 'orders/basket.html')
