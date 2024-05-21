from django.db import models
from customer.models import Customer
from product.models import Product
from django.utils import timezone

class Order(models.Model):
    LIVE = 1
    DELETE = 2
    STATUS_CHOICES = (
        (LIVE, "Live"),
        (DELETE, "Delete"),
    )

    ORDER_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4

    ORDER_STATUS_CHOICES = (
        (ORDER_STAGE, "Order Stage"),
        (ORDER_CONFIRMED, "Order Confirmed"),
        (ORDER_PROCESSED, "Order Processed"),
        (ORDER_DELIVERED, "Order Delivered"),
        (ORDER_REJECTED, "Order Rejected"),
    )

    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=ORDER_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="order")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE)
    total_price = models.FloatField(default=0)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "order - {} - {}".format(self.id, self.owner)

class OrderItem(models.Model):
    LIVE = 1
    DELETE = 0
    STATUS_CHOICES = (
        (LIVE,"Live"),
        (DELETE, "Delete"), 
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="added_cart")
    quantity =models.IntegerField(default = 1)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="added_items")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
