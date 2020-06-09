from django.contrib import admin

from .models import *

# Admin Action Function - mark as completed
def order_complete(modeladmin, request, queryset):
    queryset.update(active = 'N')

# Action description
order_complete.short_description = "Mark order as complete"

class OrderAdmin(admin.ModelAdmin):
    # list_display = ('order_id', 'user_id', 'pizItems', 'subItems', 'pastaItems', 'saladItems', 'platItems', 'time_placed', 'cost', 'active')
    list_display = ('order_id', 'user_id', 'time_placed', 'cost', 'active')
    actions = [order_complete]

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ', 'category', 'smPrice', 'lgPrice', 'numTop')
    list_editable = ('smPrice', 'lgPrice', 'numTop')

class SubAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ', 'smPrice', 'lgPrice')
    list_editable = ('smPrice', 'lgPrice')

class ExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ', 'price')
    list_editable = ['price']

class PastaAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ', 'price')
    list_editable = ['price']

class SaladAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ', 'price')
    list_editable = ['price']

class PlatterAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ','smPrice', 'lgPrice')
    list_editable = ('smPrice', 'lgPrice')

admin.site.register(Orders, OrderAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Toppings)
admin.site.register(Sub, SubAdmin)
admin.site.register(Extras, ExtraAdmin)
admin.site.register(Pasta, PastaAdmin)
admin.site.register(Salad, SaladAdmin)
admin.site.register(Platter, PlatterAdmin)

admin.site.site_header = "Pizza Orders & Administration"
