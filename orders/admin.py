from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ('order_number', 'timestamp')
    fields = ['order_number', 'buyer', 'seller', 'amount', 'status', 'delivery_location', 'timestamp']
    list_display = ['id', 'order_number', 'status', 'amount', 'seller', 'buyer']
    list_display_links = ['id', 'order_number']
    list_filter = ['status', 'buyer', 'seller']

admin.site.register(Order, OrderAdmin)
