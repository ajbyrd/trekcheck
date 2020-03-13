from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Brand(models.Model):

    brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("brand")
        verbose_name_plural = ("brands")

    def __str__(self):
        return f"{self.brand_name}"