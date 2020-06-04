from django.db import models
from django.contrib.auth.models import User


# orders
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    pizItems = models.ManyToManyField('PizOrder', blank=True, related_name='pizItems')
    subItems = models.ManyToManyField('Sub', blank=True, related_name='subItems')
    pastaItems = models.ManyToManyField('Pasta', blank=True, related_name='pastaItems')
    saladItems = models.ManyToManyField('Salad', blank=True, related_name='saladItems')
    platItems = models.ManyToManyField('Platter', blank=True, related_name='platItems')
    time_placed = models.TimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default='00.00')
    active = models.CharField(max_length=1, default='Y')

    def __str__(self):
        return f"{self.order_id} {self.user_id} {self.time_placed} {self.active} -- ${self.cost}"


# pizza menu model to include regular and sicilian
class Pizza(models.Model):
    typ = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    smPrice = models.DecimalField(max_digits=4, decimal_places=2, default='00.00')
    lgPrice = models.DecimalField(max_digits=4, decimal_places=2, default='00.00')
    numTop = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.typ} {self.category} {self.numTop} small = ${self.smPrice} large = ${self.lgPrice}"

# pizza orders
class PizOrder(models.Model):
    orderID = models.ManyToManyField('Orders', related_name='pizOrders')
    typ = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    size = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=4, decimal_places=2, default='00.00')
    toppings = models.ManyToManyField('Toppings', blank=True, related_name='customPiz')

    def __str__(self):
        return f"{self.orderID} {self.typ} {self.category} {self.size} {self.toppings} ${self.price}"


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
