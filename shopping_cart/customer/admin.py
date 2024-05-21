from django.contrib import admin
from .models import Customer , User

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'user', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'address', 'phone')
    list_filter = ('created_at', 'updated_at')
    ordering = ('created_at',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(User)
