from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class Connection(models.Model):

    # Atributos del modelo conexión
    connection_name = models.CharField(max_length=50)
    host = models.CharField(max_length=16)
    port = models.IntegerField()
    manager_db = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50, blank=True)
    dbname = models.CharField(max_length=50)
    dbname2 = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 
    
    def get_absolute_url(self):
        return reverse('list-connections')
