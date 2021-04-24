import time
from django.db import models
from store.models import PaymentMethod


class Order(models.Model):
    Status_Choices = [
        ('pending', 'pending'),
        ('paid', 'paid'),
        ('processing', 'processing'),
        ('cancelled', 'cancelled'),
        ('refunded', 'refunded'),
    ]

    seller = models.CharField(max_length=100)
    buyer = models.CharField(max_length=100)
    order_number = models.CharField(max_length=120, unique=True)
    delivery_location = models.CharField(max_length=255, blank=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, null=True, blank=True)
    products = models.TextField(default=[], help_text="A list of products from a cart (if it exists).")
    quantity = models.PositiveIntegerField(default=1, help_text="Number of products in list of products from cart.")
    status = models.CharField(max_length=20, default="Undefined", choices=Status_Choices)
    amount = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ord_num = round(time.time() * 99)
        if not self.pk:
            self.order_number = "COL-"+str(ord_num)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.order_number}'
