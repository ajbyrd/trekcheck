from django.db import models

class Category(models.Model):

    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return f"{self.category_name}"