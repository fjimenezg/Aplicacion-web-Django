from django.db import models
from django.urls import reverse
from global_.manager_connection import ManagerConnection
from app_connection.models import Connection
import ast

# Create your models here.

# Modelo principal de servicios.
class Service(models.Model):
    kinds = (
        ('sqlquery', 'Consulta SQL'),
        ('item', 'Objetos Perdidos'),
        ('directory', 'Directorio de Dependencias'),
        ('localization', 'Geolocalizacion de Bloques'),
    )

    name = models.CharField(max_length=100, unique=True)
    kind = models.CharField(max_length=20, choices=kinds)
    permits = models.IntegerField()
    state = models.BooleanField()
    unique_key = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=300, blank=True)
    roles = models.CharField(max_length=100, blank=True)
    links = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service-list')


# Modelo de configuracion de servicios de consulta SQL
class SQLQuery(models.Model):
    Service = models.OneToOneField(Service, primary_key=True, on_delete="CASCADE",
                                    limit_choices_to={'kind': 'sqlquery'},
                                    related_name="query", related_query_name="query")
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=50, unique=True)
    query_sql = models.CharField(max_length=300)
    description_fields = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name = "Query"
        verbose_name_plural = "Queries"

    def __str__(self):
        return self.type_name

    def get_absolute_url(self):
        return reverse("base-service")

    def is_active(self):
        connection = ManagerConnection(**self.connection.get_data_connection())
        return connection.check_connection()

    def get_fields_service(self):
        connection = ManagerConnection(**self.connection.get_data_connection())
        return connection.getColumns(self.query_sql)

    def get_list_search(self, filter={}):
        connection = ManagerConnection(**self.connection.get_data_connection())
        data = connection.managerSQL(self.query_sql)
        if data is not None:
            if len(filter) > 0:
                for key, value in filter.items():
                    filtered_data = []
                    for fact in data:
                        if str(fact[key]) == str(value):
                            filtered_data.append(fact)
                    data = filtered_data
            return data
        return None

    def get_links(self):
        if len(self.links) > 0:
            try:
                dict_links = ast.literal_eval(self.links)
                if type(dict_links) is type({}):
                    return dict_links
                return None
            except:
                return None

# Modelos de items individuales, asociados a un servicio general de Objetos Perdidos, Directorio y Geolocalizacion
class MissingItem(models.Model):
    Service = models.ForeignKey(Service, on_delete="CASCADE",
                                limit_choices_to={'kind': 'item'},
                                related_name="items", related_query_name="item")
    name = models.CharField(max_length=100) 
    description = models.CharField(max_length=200) 
    date = models.DateField(auto_now_add=True)
    photo = models.ImageField(blank=True, upload_to='photos')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-list')

class Office(models.Model):
    Service = models.ForeignKey(Service, on_delete="CASCADE",
                                limit_choices_to={'kind': 'directory'},
                                related_name="offices", related_query_name="office")
    name = models.CharField(max_length=100)
    extension = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('office-list')

class Location(models.Model):
    Service = models.ForeignKey(Service, on_delete="CASCADE",
                                limit_choices_to={'kind': 'localization'},
                                related_name="locations", related_query_name="location")
    name = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('location-list')




