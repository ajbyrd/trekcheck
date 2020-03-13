from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

class User(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length = 25, null=True)
    email = models.CharField(max_length = 40, null=True)
    first_name = models.CharField(max_length = 25, null=True)
    last_name = models.CharField(max_length = 25, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'