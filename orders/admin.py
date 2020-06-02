from django.contrib import admin

from .models import Orders, Pizza, Toppings, Sub, Extras, Pasta, Salad, Platter

admin.site.register(Orders)
admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Sub)
admin.site.register(Extras)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Platter)