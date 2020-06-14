from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

import json


def home(request):
    return render(request, 'orders/home.html')


def register(request):

    if request.method == 'POST':

        first = request.POST["first"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(username, email, password)

        user.first_name = first
        user.last_name = surname
        user.save()

        login(request, user)

        return HttpResponseRedirect(reverse("menu"))

    else:
        return render(request, 'orders/register.html')


def log_in(request):

    if request.method == 'POST':

        username = request.POST["un"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("menu"))
        else:
            return render(request, "users/login.html", {"message": "Invalid username/password."})

    else:
        logout(request)
        return render(request, 'orders/login.html')


def log_out(request):

    logout(request)
    return render(request, 'orders/login.html', {'success': 'Successfully logged out!'})


def menu(request):

    if request.user.is_authenticated:

        if request.method == 'GET':

            # django won't allow range in template {% %} of html page hence defining it here
            it = Pizza.objects.all()

            # iterate over pizas and add column for ranges
            for row in it:
                num = row.numTop
                row.num = range(1, (num+1))

            context = {
                "user": request.user,
                "pizza": it,
                "toppings": Toppings.objects.all(),
                "subs": Sub.objects.all(),
                "extras": Extras.objects.all(),
                "pasta": Pasta.objects.all(),
                "salads": Salad.objects.all(),
                "platters": Platter.objects.all()
            }
            return render(request, "orders/menu.html", context)

    else:
        return render(request, "orders/menu.html")


def place(request):

    if request.user.is_authenticated:

        if request.method == 'POST':

            user = request.user
            data = request.POST['hiddenData']

            data = json.loads(data)

            ord1 = Orders(user_id=user)
            ord1.save()

            for row in data:
                if row['item'] == 'Pizza':
                    p1 = Pizza.objects.get(id=row['ident'])

                    po1 = PizOrder(order_id=ord1, typ=p1, price=float(row['price']), size=row['size'])
                    po1.save()

                    if row['toppings'] != []:
                        for row in row['toppings']:
                            top = Toppings.objects.get(typ=row.replace('&amp;', '&'))
                            po1.toppings.add(top)
                            po1.save()

                    ord1.cost += po1.price
                    ord1.pizItems.add(po1)
                    ord1.save()

                elif row['item'] == 'Sub':
                    s1 = Sub.objects.get(id=row['ident'])

                    so1 = SubOrder(order_id=ord1, 
                        typ=s1, price=float(row['price']), size=row['size'])
                    so1.save()

                    if row['toppings'] != []:
                        for row in row['toppings']:
                            row = Extras.objects.get(typ=row.replace('&amp;', '&'))
                            so1.extras.add(row)
                            so1.save()

                    ord1.cost += so1.price
                    ord1.subItems.add(so1)
                    ord1.save()

                elif row['item'] == 'Pasta':
                    pasta1 = Pasta.objects.get(id=row['ident'])

                    paO1 = PastaOrder(order_id=ord1, 
                        typ=pasta1, price=float(row['price']))
                    paO1.save()

                    ord1.cost += paO1.price
                    ord1.pastaItems.add(paO1)
                    ord1.save()

                elif row['item'] == 'Salad':
                    salad1 = Salad.objects.get(id=row['ident'])

                    salO1 = SaladOrder(order_id=ord1, 
                        typ=salad1, price=float(row['price']))
                    salO1.save()

                    ord1.cost += salO1.price
                    ord1.saladItems.add(salO1)
                    ord1.save()

                elif row['item'] == 'Platter':
                    platter1 = Platter.objects.get(id=row['ident'])

                    plato1 = PlatterOrder(order_id=ord1, 
                        typ=platter1, price=float(row['price']), size=row['size'])
                    plato1.save()

                    ord1.cost += plato1.price
                    ord1.platItems.add(plato1)
                    ord1.save()

                else:
                    continue

            return HttpResponseRedirect(reverse("basket"))

    else:
        return HttpResponseRedirect(reverse("login"))


def basket(request):

    user = request.user

    active = Orders.objects.filter(
        user_id=user, active='Y').order_by('-time_placed')
    delivery = Orders.objects.filter(
        user_id=user, active='D').order_by('-time_placed')
    expired = Orders.objects.filter(
        user_id=user, active='N').order_by('-time_placed')
    
    pizzas = PizOrder.objects.all()
    subs = SubOrder.objects.all()
    pastas = PastaOrder.objects.all()
    salads = SaladOrder.objects.all()
    platters = PlatterOrder.objects.all()

    context = {
        "user": user,
        "active": active,
        "delivery": delivery,
        "expired": expired,
        "pizzas": pizzas,
        "subs": subs,
        "pastas": pastas,
        "salads": salads,
        "platters": platters
    }

    return render(request, 'orders/basket.html', context)
