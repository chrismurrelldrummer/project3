from django.contrib import admin

from .models import *

# Admin Action Function - mark as completed
def order_complete(modeladmin, request, queryset):
    queryset.update(active = 'N')
# Action description
order_complete.short_description = "Mark order as complete"

# Admin Action Function - mark as delivery
def order_delivery(modeladmin, request, queryset):
    queryset.update(active = 'D')
# Action description
order_delivery.short_description = "Mark order as out for delivery"

class PizInline(admin.StackedInline):
      model = Orders.pizItems.through

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'email', 'time_placed', 'cost', 'active')
    list_select_related = ['user_id']
    actions = (order_complete, order_delivery)
    inlines = [PizInline]

    def email(self, instance):
        return instance.user_id.email

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ', 'category', 'smPrice', 'lgPrice', 'numTop')
    list_editable = ('smPrice', 'lgPrice', 'numTop')

class PizItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'typ', 'size', 'toppings', 'price')

    def order(self, instance):
        return instance.order_id
    
    def toppings(self, instance):
        return instance.toppings.typ

class SubAdmin(admin.ModelAdmin):
    list_display = ('id', 'typ', 'smPrice', 'lgPrice')
    list_editable = ('smPrice', 'lgPrice')

class ExtraAdmin(admin.ModelAdmin):
    list_display = ('typ', 'price')
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

admin.site.register(PizOrder, PizItemAdmin)
admin.site.register(SubOrder)
admin.site.register(PastaOrder)
admin.site.register(SaladOrder)
admin.site.register(PlatterOrder)

admin.site.site_header = "Pizza Orders & Administration"
