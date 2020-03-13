from django.db import models

class TripItem(models.Model):

    trip = models.ForeignKey("Trip", on_delete=models.CASCADE)
    item = models.ForeignKey("InventoryItem", on_delete=models.CASCADE)

    class Meta:
        ordering = ("trip",)