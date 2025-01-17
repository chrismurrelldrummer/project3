from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.log_in, name="login"),
    path("logout", views.log_out, name="logout"),
    path("menu", views.menu, name="menu"),
    path("basket", views.basket, name="basket"),
    path("place", views.place, name="place"),
    path("account", views.account, name="account"),
    path("account/filter/<filter_by>", views.filter, name="filter"),
]
