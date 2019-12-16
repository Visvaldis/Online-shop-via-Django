from django.contrib import admin
from .models import Order, OrderDetails


# Register your models here.


# Define the admin class
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_date', 'summa', 'customer')


# Register the admin class with the associated model
admin.site.register(Order, OrderAdmin)


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('details_id', 'order', 'product', 'product_amount', 'summa')


# Register the admin class with the associated model
admin.site.register(OrderDetails, OrderDetailsAdmin)
