from django.db import models
from .customer import Customer
from django.urls import reverse

class Trip(models.Model):


    trip_name = models.CharField(max_length=50)
    trip_date = models.DateField()
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("trip")
        verbose_name_plural = ("trips")

    def __str__(self):
        return self.trip_name

    

