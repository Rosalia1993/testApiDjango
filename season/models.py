from django.db import models

# Create your models here.

class SeasonStatus(models.Model):
    order_id = models.CharField(max_length=70)
    order_date = models.DateField()
    qt_ordd = models.IntegerField()