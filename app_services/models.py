from django.db import models
from django.urls import reverse
from global_.manager_connection import ManagerConnection
from app_connection.models import Connection
import ast

# Create your models here.

class Service(models.Model):
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=50, unique=True)
    service_name = models.CharField(max_length=50, unique=True)
    query_sql = models.CharField(max_length=300)
    unique_key = models.CharField(max_length=50, blank=True)
    icon = models.CharField(max_length=100, blank=True)
    description_fields = models.CharField(max_length=300, blank=True)
    links = models.CharField(max_length=300, blank=True)
    roles = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

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





