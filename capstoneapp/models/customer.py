from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length = 25, null=True)
    email = models.CharField(max_length = 40, null=True)
    first_name = models.CharField(max_length = 25, null=True)
    last_name = models.CharField(max_length = 25, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


    # Every time a `User` is created, a matching `Librarian`
    # object will be created and attached as a one-to-one
    # property
    @receiver(post_save, sender=User)
    def create_customer(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    # Every time a `User` is saved, its matching `Librarian`
    # object will be saved.
    @receiver(post_save, sender=User)
    def save_customer(sender, instance, **kwargs):
        instance.customer.save()