from django.contrib import admin

from .models import Pizza, Toppings, PizItem

admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(PizItem)
