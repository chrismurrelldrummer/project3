from django.db import models
from django.contrib.auth.models import User


# orders
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    pizItems = models.ManyToManyField('Pizza', related_name='pizItems')
    subItems = models.ManyToManyField('Sub', related_name='subItems')
    pastaItems = models.ManyToManyField('Pasta', related_name='pastaItems')
    saladItems = models.ManyToManyField('Salad', related_name='saladItems')
    platItems = models.ManyToManyField('Platter', related_name='platItems')
    time_placed = models.TimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default='00.00')
    active = models.CharField(max_length=1, default='Y')

    def __str__(self):
        return f"{self.order_id} {self.user_id} {self.time_placed} {self.active} -- ${self.cost}"


# pizza menu model to include regular and sicilian
class Pizza(models.Model):
    typ = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    size = models.CharField(max_length=5)
    toppings = models.ManyToManyField('Toppings', related_name='pizzas')
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.typ} {self.category} {self.size} {self.toppings} -- ${self.price}"


# pizza toppings model
class Toppings(models.Model):
    typ = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.typ}"


# sub orders
class Sub(models.Model):
    typ = models.CharField(max_length=64)
    size = models.CharField(max_length=5)
    extras = models.ManyToManyField('Extras', related_name='subs')

    def __str__(self):
        return f"{self.typ} + {self.size}"


# extras orders
class Extras(models.Model):
    typ = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.typ}"


# pasta orders
class Pasta(models.Model):
    typ = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.typ} -- ${self.price}"


# salad orders
class Salad(models.Model):
    typ = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.typ} -- ${self.price}"


# platter orders
class Platter(models.Model):
    typ = models.CharField(max_length=64)
    size = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.typ} {self.size} -- ${self.price}"
