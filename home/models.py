from django.db import models

# Create your models here.
class Item(models.Model):
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=None, decimal_places=2)