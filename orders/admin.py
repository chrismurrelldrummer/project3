from django.contrib import admin

from .models import *

# # Admin Action Functions
# def change_price(modeladmin, request, queryset):
#     queryset.update(smPrice = '19.99')

# # Action description
# change_price.short_description = "Update Small price to 19.99"


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ', 'category', 'smPrice', 'lgPrice', 'numTop')
    list_editable = ('typ', 'category', 'smPrice', 'lgPrice', 'numTop')
    #   actions = [change_price]


admin.site.register(Orders)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Toppings)
admin.site.register(Sub)
admin.site.register(Extras)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Platter)
