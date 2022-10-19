from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Stats(models.Model):
    stat_id = models.CharField(max_length =50, primary_key=True, null=False)
    city_id = models.IntegerField(null=False)
    date = models.DateField(null=False)
    avg_m2_price_primary = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    avg_m2_price_after = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    avg_m2_price_all = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    avg_unit_price_primary = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    avg_unit_price_after = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    avg_unit_price_all = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    count_primary = models.IntegerField(null=False)
    count_after = models.IntegerField(null=False)
    count_all = models.IntegerField(null=False)