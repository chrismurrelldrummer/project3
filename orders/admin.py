from django.contrib import admin

from .models import *

# # Admin Action Functions
# def change_price(modeladmin, request, queryset):
#     queryset.update(smPrice = '19.99')

# # Action description
# change_price.short_description = "Update Small price to 19.99"


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ', 'category', 'smPrice', 'lgPrice', 'numTop')
    list_editable = ('smPrice', 'lgPrice', 'numTop')
    #   actions = [change_price]

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

admin.site.register(Orders)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Toppings)
admin.site.register(Sub, SubAdmin)
admin.site.register(Extras, ExtraAdmin)
admin.site.register(Pasta, PastaAdmin)
admin.site.register(Salad, SaladAdmin)
admin.site.register(Platter, PlatterAdmin)

admin.site.site_header = "Pizza Orders & Administration"
