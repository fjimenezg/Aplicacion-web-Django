from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    name = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name

