from django.db import models
from customer.models import Customer

# Create your models here.
class Order(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    total_price = models.FloatField(null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    order_status = models.CharField(max_length=100)
