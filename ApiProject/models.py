from django.db import models

class OrderStatus(models.Model):
    order_number = models.CharField(max_length=10)
    item_name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

