from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner', 'status', 'total_price', 'created', 'updated', 'order_status')
    search_fields = ('owner__name', 'status', 'order_status')
    list_filter = ('status', 'created', 'updated')
    ordering = ('created',)

admin.site.register(Order, OrderAdmin)

