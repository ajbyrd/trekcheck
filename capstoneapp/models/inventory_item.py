from django.db import models
from .brand import Brand
from .customer import Customer
from .category import Category
from django.urls import reverse

class InventoryItem(models.Model):


    model_name = models.CharField(max_length=50)
    weight = models.FloatField()
    description = models.CharField(max_length=250)
    image_path = models.CharField(max_length=250, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("item")
        verbose_name_plural = ("items")

    def __str__(self):
        return self.model_name

    

