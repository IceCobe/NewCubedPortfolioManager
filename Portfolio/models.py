from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=14, decimal_places=4)