from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Orders, Basket, Pizza, PizOrder, Toppings, Sub, Extras, Pasta, Salad, Platter



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
            # returning none *****************************************************************8
            typ = request.POST.get("typ")
            cat = request.POST.get("cat")

            toppings = []
            maxTop = 0

            # find max number of possible toppings
            piz = Pizza.objects.all()

            for row in piz:
                num = row.numTop
                if num > maxTop:
                    maxTop = num
            
            for i in range(1,(maxTop + 1)):
                try:
                    top = request.POST[f"customTop{i}"]
                    toppings.append(top)
                except:
                    continue

            try:
                size = request.POST["small"]
                price = request.POST["smplace"]
            except:
                size = request.POST["large"]
                price = request.POST["lgplace"]

            user = request.user

            # if order/basket already active for user

            context = {
                "user": user.username,
                "typ": typ,
                "cat": cat,
                "tops": toppings,
                "size": size,
                "price": price
            }

            return render(request, "orders/menu.html", {'message': context})

    else:
        return render(request, "orders/menu.html")


def basket(request):
    return render(request, 'orders/basket.html')
