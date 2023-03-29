from django.db import models

# Create your models here.

PAYMENT_STATUS = [
    ("PENDING", "PENDING"),
    ("SUCCESS", "SUCCESS"),
]

PAYMENT_MODE = [
    ("COD", "COD"),
    ("MOMO", "MOMO"),
]

class Payment(models.Model):
    order_id = models.IntegerField()
    user_id = models.IntegerField()
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=15, default="PENDING", choices=PAYMENT_STATUS)
    payment_mode = models.CharField(max_length=15, choices=PAYMENT_MODE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment: {self.id}"