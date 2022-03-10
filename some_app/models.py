from django.db import models


class Product(models.Model):
    low_price = models.DecimalField(max_digits=7, decimal_places=2)
    high_price = models.DecimalField(max_digits=7, decimal_places=2)

    demand_qty = models.IntegerField()
    offers_qty = models.IntegerField()

    bought_qty = models.IntegerField()
    sold_qty = models.IntegerField()

    time_created = models.DateTimeField()

    class Meta:
        ordering = ('time_created',)
