from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner', 'status', 'total_price', 'created_at', 'updated_at', 'order_status')
    search_fields = ('owner__name', 'status', 'order_status')
    list_filter = ('status', 'created_at', 'updated_at')
    
admin.site.register(Order, OrderAdmin)

