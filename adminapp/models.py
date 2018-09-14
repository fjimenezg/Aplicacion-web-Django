from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from .manager_connection import ManagerConnection
import ast

# Create your models here.


class Connection(models.Model):

    managers = (("mysql", "MySQL"), ("postgresql", "postgreSQL"), ("oracle", "Oracle"))

    # Atributos del modelo conexión
    connection_name = models.CharField(max_length=50, unique=True)
    host = models.CharField(max_length=16)
    port = models.IntegerField()
    manager_db = models.CharField(max_length=50, choices=managers)
    user = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50, blank=True)
    dbname = models.CharField(max_length=50)

    def __str__(self):
        return self.connection_name

    def get_data_connection(self):
        return {
            "host": self.host,
            "port": self.port,
            "manager_db": self.manager_db,
            "user": self.user,
            "passwd": self.passwd,
            "dbname": self.dbname,
        }

    def get_absolute_url(self):
        return reverse("list-connections")


class Service(models.Model):
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=50, unique=True)
    class_name = models.CharField(max_length=50, blank=True)
    query_sql = models.CharField(max_length=300)
    links = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.service_name

    def is_active(self):
        connection = ManagerConnection(**self.connection.get_data_connection())
        return connection.check_connection()

    def get_fields_service(self):
        connection = ManagerConnection(**self.connection.get_data_connection())
        return connection.getColumns(self.query_sql)

    def get_list_search(self, filter={}):
        connection = ManagerConnection(**self.connection.get_data_connection())
        data = connection.managerSQL(self.query_sql)
        print(filter)
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

    def get_field_search(self, key, value):  
        connection = ManagerConnection(**self.connection.get_data_connection())    
        data = connection.managerSQL(self.query_sql)
        for fact in data:
            if str(fact[key]) == value:
                return fact
        return None

    def get_links(self):
        if len(self.links) > 0:
            dict_links = ast.literal_eval(self.links)
            if type(dict_links) is type({}):
                return dict_links
        return None


class Relationship(models.Model):
    """Model definition for Relationship."""

    # TODO: Define fields here
    unique_item_search = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Relationship."""

        verbose_name = "Relationship"
        verbose_name_plural = "Relationships"

    def __str__(self):
        """Unicode representation of Relationship."""
        pass
