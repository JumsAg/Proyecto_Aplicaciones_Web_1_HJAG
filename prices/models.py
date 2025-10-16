from django.db import models

from django.db import models

class WatchItem(models.Model):
    name = models.CharField("Nombre", max_length=50)      # Ej: Bitcoin
    symbol = models.CharField("Símbolo", max_length=20)   # Ej: btc
    target_price = models.DecimalField(
        "Precio objetivo", max_digits=12, decimal_places=2, null=True, blank=True
    )
    notes = models.TextField("Notas", blank=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"
