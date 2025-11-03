from django.db import models

class WatchItem(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    target_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.name} ({self.symbol})"
