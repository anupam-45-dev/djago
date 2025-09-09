# admin.py
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'table', 'status', 'total','address', 'time')
    list_filter = ('status', 'time')

admin.site.register(Order, OrderAdmin)  # <-- Use OrderAdmin class
from orders.models import Order
Order.objects.all()
