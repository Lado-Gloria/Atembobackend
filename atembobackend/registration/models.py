from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(Group, related_name='farmers_related', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='farmers_related', blank=True)

    def __str__(self):
        return self.username